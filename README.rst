c2c.recipe.closurecompile
=========================

Compress javascript files using the `Google Closure Compiler
<http://code.google.com/closure/compiler/>`_

Usage
-----

Minimal buildout config example::

    [buildout]
    parts = closure-compile

    [closure-compile]
    recipe = c2c.recipe.closurecompile
    compiler = path/to/closure-compiler.jar
    level = SIMPLE_OPTIMIZATIONS
    source_map = foo/bar.map
    externs = externs/a.js externs/b.js
    input = foo/bar.js
    output = foo/bar.min.js
    output_mode = compiled

Where:

  * ``compiler``: The location of the compiler jar file.
  * ``level``: The compilation level: ``WHITESPACE_ONLY``,
    ``SIMPLE_OPTIMIZATIONS`` or ``ADVANCED_OPTIMIZATIONS``. Default is
    ``WHITESPACE_ONLY``.
  * ``source_map``: Path to the source map file. Optional.
  * ``externs``: A list of optional externs files.
  * ``input``: The files to compress separated with spaces. The path
    can be absolute or relative to the buildout directory. These files
    are also used to calculate the dependencies in addition to the
    ``namespace`` option.
  * ``root``: The list of paths that should be traversed to build the
    dependencies.
  * ``namespace``: One or more namespaces to calculate dependencies for.
  * ``output``: The path to the minified file.
  * ``output_mode``: The type of output to generate from this script.
    Options are "list" for a list of filenames, "script" for a single
    script containing the contents of all the files, or "compiled" to
    produce compiled output with the Closure Compiler.  Default is
    "compiled".

Getting the jar
---------------

To automatically download and unzip the compiler from Google, you can
use the ``hexagonit.recipe.download`` receipt::

    [buildout]
    parts = closure-compile

    [closure-compile]
    recipe = c2c.recipe.closurecompile
    compiler = ${download-closure-compile:destination}/compiler.jar
    ...

    [download-closure-compile]
    recipe = hexagonit.recipe.download
    url = http://closure-compiler.googlecode.com/files/compiler-latest.zip
