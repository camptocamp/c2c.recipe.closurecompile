import os
import tempfile
import logging
from subprocess import call, STDOUT
import zc.buildout

from c2c.recipe.closurecompile.goog import treescan
from c2c.recipe.closurecompile.goog import source
from c2c.recipe.closurecompile.goog import depstree

class PathSource(source.Source):
    def __init__(self, path):
        super(PathSource, self).__init__(source.GetFileContents(path))
        self._path = path

    @property
    def path(self):
        return self._path


class ClosureCompile(object):
    def __init__(self, buildout, name, options):
        self.name = name
        basedir = buildout['buildout']['directory']

        self.compiler = options.get('compiler')

        self.source_map = os.path.join(basedir, options.get('source_map')) if options.get('source_map') else None

        self.inputs = [os.path.join(basedir, f) for f in options.get('input', '').split()]
        self.roots = [os.path.join(basedir, f) for f in options.get('root', '').split()]
        self.externs = [os.path.join(basedir, f) for f in options.get('externs', '').split()]

        self.namespaces = options.get('namespace', '').split()

        self.output = os.path.join(basedir, options.get('output'))

        self.level = options.get('level', 'WHITESPACE_ONLY')
        self.output_mode = options.get('output_mode', 'compiled')

    def install(self):
        installed_files = []

        installed_files.append(self.output)

        sources = set()
        for path in self.roots:
            for js_path in treescan.ScanTreeForJsFiles(path):
                sources.add(PathSource(js_path))

        for js_path in self.inputs:
            sources.add(PathSource(js_path))

        # get namespaces from namespace and input options
        namespaces = set(self.namespaces)
        for js_path in self.inputs:
            namespaces.update(PathSource(js_path).provides)

        if not namespaces:
            # no namespaces found: the compiled code do not use the Closure Library
            deps = sources
        else:
            deps = depstree.DepsTree(sources).GetDependencies(namespaces)
            # The Closure Library base file must go first (if present).
            base = next((s for s in sources if os.path.basename(s.path) == 'base.js' and 'goog' in s.provides), None)
            if base is not None:
                deps = [base] + deps

        if self.output_mode == 'list':
            file(self.output, 'w').writelines([source.path + '\n' for source in deps])
        elif self.output_mode == 'script':
            file(self.output, 'w').writelines([source.GetSource() for source in deps])
        elif self.output_mode == 'compiled':
            cmd  = "java -jar %s "%self.compiler
            cmd += "--js %s "%(" --js ".join([source.path for source in deps]))
            cmd += "--js_output_file %s "%(self.output)
            if self.source_map:
                cmd += "--create_source_map %s "%self.source_map
                installed_files.append(self.source_map)
            if self.externs:
                cmd += "--externs %s "%" --externs ".join(self.externs)
            cmd += "--compilation_level %s "%self.level

            logging.getLogger(self.name).debug("running '%s'"%cmd)

            errors = tempfile.TemporaryFile()
            retcode = call(cmd.split(), stdout=errors, stderr=STDOUT)

        return installed_files

    update = install
