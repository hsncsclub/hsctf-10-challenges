#!/usr/bin/env python3
import ast
import sys

# from more_itertools
def split_before(iterable, pred, maxsplit=-1):
	if maxsplit == 0:
		yield list(iterable)
		return
	
	buf = []
	it = iter(iterable)
	for item in it:
		if pred(item) and buf:
			yield buf
			if maxsplit == 1:
				yield [item] + list(it)
				return
			buf = []
			maxsplit -= 1
		buf.append(item)
	if buf:
		yield buf

with open(sys.argv[1], encoding="utf-8") as f:
	lines = f.readlines()

# 1 bit for const vs instruction, 7 bits for 2 instructions -> elevens digit and ones digit
instructions = [
	"NOP",
	"JNZ_REAL",  # pop 2, and jump to 1st if 2nd is not zero
	"ADD",  # pop 2, push 2nd + 1st
	"SUB",  # pop 2, push 2nd - 1st
	"MOVL",  # pop 1, push it to the stack to the left
	"MOVR",  # pop 1, push it to the stack to the right
	"SHIFTL",  # switch current stack to the one on the left
	"SHIFTR",  # switch current stack to the one on the right
	"DUP",  # duplicate top
	"XOR",  # pop 2, push 2nd ^ 1st
	"PEEK",  # push 2 if stack has 2+ elements, 1 if stack has 1 element, 0 otherwise
]

# replace "ARRAY", "JNZ", "JUMP" with instructions and remove comments
for i, line in enumerate(lines):
	# remove comments
	line = line.split("#")[0].strip()
	if not line:
		lines[i] = []
		continue
	
	# ignore labels
	label, _, instruction = map(str.strip, line.rpartition(":"))
	if not instruction:
		print(f"Label must be followed by an instruction {line!r}")
		sys.exit(1)
	
	# this code sucks lol
	if instruction.upper().startswith("ARRAY "):
		vals = ast.literal_eval(instruction.split(maxsplit=1)[1])
		new_ins = []
		for val in vals:
			if 128 < val < 255:
				new_ins.extend([f"{label+_} PUSH {val - 127}", "PUSH 127", "ADD"])
			elif val < 0:
				new_ins.extend([f"{label+_} PUSH 0", f"PUSH {abs(val)}", "SUB"])
			else:
				new_ins.append(f"{label+_} PUSH {val}")
		lines[i] = new_ins
	elif instruction.upper().startswith("JNZ "):
		target = line.split(" ")[-1]
		lines[i] = [f"{label+_} PUSH {target}", "JNZ_REAL"]
	elif instruction.upper().startswith("JUMP "):
		target = line.split(" ")[-1]
		lines[i] = [f"{label+_} PUSH 1", f"PUSH {target}", "JNZ_REAL"]

lines = [line for line2 in lines for line in ([line2] if isinstance(line2, str) else line2)]

# align half-bytes to a full byte using NOPS

groups = split_before(lines, lambda line: line.split(":")[-1].strip().upper().startswith("PUSH "))
lines = []
for group in groups:
	# should be odd length when **not** including the PUSH, and even including the PUSH
	if group and len(group) % 2 == (
		0 if group[0].split(":")[-1].strip().upper().startswith("PUSH ") else 1
	):
		group.append("NOP")
	lines.extend(group)

# define labels
line_no = 0
labels = {}

for line in lines:
	if ":" in line:
		label, _, instruction = map(str.strip, line.partition(":"))
		labels[label] = line_no
	line_no += 1

# encode instructions
encoded: list[int] = []
prev_ins = None
for line in lines:
	# ignore comments and labels
	instruction = line.split("#")[0].split(":")[-1].strip()
	if not instruction:
		continue
	
	if instruction.upper().startswith("PUSH "):
		if prev_ins is not None:
			print(f"Invalid padding before {instruction!r}")
			sys.exit(1)
		
		arg = instruction.split(" ")[-1]
		if not arg.isdigit():
			arg = labels[arg]
		
		val = int(arg)
		if val > 128 or val < 0:
			print(lines[lines.index(line) - 1:lines.index(line) + 2])
			print(f"Invalid value {val!r}")
			sys.exit(1)
		
		encoded.append(val | (1 << 7))
	else:
		ins_encoded = instructions.index(instruction.upper())
		
		if prev_ins is not None:
			encoded.append(prev_ins * 11 + ins_encoded)
			prev_ins = None
		else:
			prev_ins = ins_encoded

if prev_ins is not None:
	print("Invalid final padding")

with open("asm.out", "wb") as f:
	f.write(bytes(encoded))