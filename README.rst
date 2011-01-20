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
    input = foo/bar.js
    output = foo/bar.min.js

Where:

  * ``compiler``: The path to the compiler jar file.
  * ``level``: The compilation level: ``WHITESPACE_ONLY``,
    ``SIMPLE_OPTIMIZATIONS`` or ``ADVANCED_OPTIMIZATIONS``. Default is
    ``WHITESPACE_ONLY``.
  * ``input``: The files to compress separated with spaces. The path
    can be absolute or relative to the buildout directory.
  * ``output``: The path to the minified file. If omitted, the result
    is saved to ``input`` (which must be unique).


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
