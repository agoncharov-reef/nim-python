#!/bin/sh
nim c -d:ssl --threads:on --app:lib --out:nimlib.so nimlib.nim
