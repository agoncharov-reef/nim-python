# nim-python

A demo app to show how to run Nim code from within Python.

1. Install nimpy: `nimble install nimpy`
2. Compile `.nim` sources to shared library: `nim c -d:ssl --threads:on --app:lib --out:nimlib.so nimlib.nim`
3. Use it in Python as usual module: `import nimlib; nimlib.get(url)`
