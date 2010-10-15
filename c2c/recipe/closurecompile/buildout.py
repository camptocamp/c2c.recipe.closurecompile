import os
import tempfile
from subprocess import call, STDOUT

class ClosureCompile(object):
    def __init__(self, buildout, name, options):
        self.name = name
        basedir = buildout['buildout']['directory']

        self.compiler = options.get('compiler')
        # fixme: validate self.compiler
        self.input = [os.path.join(basedir, f) for f in options.get('input').split()]
        self.output = os.path.join(basedir, options.get('output'))
        self.level = options.get('level', 'WHITESPACE_ONLY')
        

    def install(self):
        cmd = "java -jar %(compiler)s --js %(input)s --js_output_file %(output)s --compilation_level %(level)s"

        tmpdir = tempfile.mkdtemp()
        errors = tempfile.TemporaryFile()
        retcode = call(cmd.split(), stdout=errors, stderr=STDOUT)

        return self.output
        
    update = install

