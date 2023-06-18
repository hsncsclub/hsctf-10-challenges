#!/bin/bash
python3 asm.py src.asm
stack ghc vm.hs
python3 -c 'b = open("vm", "rb").read(); print("#define PROGRAM {" + ",".join(str(c ^ 26) for c in b)+ "}"); print(f"#define LENGTH {len(b)}")' > data.h
gcc wrapper.c -o recursed
