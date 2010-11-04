Usage
-----
Minimal buildout config example:

[buildout]
parts = jsbuild

[jsbuild]
recipe = c2c.recipe.closurecompile
compiler = ${closure-compile:destination}/compiler.jar
level = SIMPLE_OPTIMIZATIONS
input = foo/bar.js
output = foo/bar.min.js

[closure-compile]
recipe = hexagonit.recipe.download
url = http://closure-compiler.googlecode.com/files/compiler-latest.zip

'level' is WHITESPACE_ONLY, SIMPLE_OPTIMIZATIONS or
ADVANCED_OPTIMIZATIONS,  defaults is WHITESPACE_ONLY.

If 'output' is not specified, the minified version is written into 'input'.
