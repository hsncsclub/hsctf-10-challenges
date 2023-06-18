#!/bin/bash
rm __pycache__/chall.cpython-38.pyc
python3.8 -m py_compile chall.py
cp __pycache__/chall.cpython-38.pyc micrurus-fulvius.pyc
python3.8 micrurus-fulvius.pyc < flag.txt
