#!/usr/bin/env python3
flag = 46327402297733866529555553960981046817278883618336227619492913845039231366013

def f(x):
	s = str(x)
	k = len(s)//2
	return "#"*(len(s)-k) + s[k:]

print("Welcome to the Half-Calculator")
print("Operations:")
print("    * x : multiplies by x")
print("    / x : divides by x")
print("    ++ : adds one")
print("    -- : subtracts one")
print()
print("printing variable ... FLAG")
print()
print(f(flag))
print()

try:
	i = 0
	while i < 6:
		x = input("Operation: ")
		l = x.split()
		if len(l) < 1: 
			print("Invalid input")
		elif l[0] == "*":
			u = int(l[1])
			flag *= u
			print(f(flag))
			i += 1
		elif l[0] == "/":
			u = int(l[1])
			if flag % u == 0:
				flag //= u
				print(f(flag))
				i += 1
			else:
				print("ERROR: divisibility check failed")
		elif l[0] == "++":
			flag += 1
			print(f(flag))
			i += 1
		elif l[0] == "--":
			flag -= 1
			print(f(flag))
			i += 1
		else:
			print("Invalid input")
		print()
	print("ERROR: LOW BATTERY")
except:
	print("unknown error")
