import hashlib

def a(n):
	b = 0
	while n != 1:
		if n & 1:
			n *= 3
			n += 1
		else:
			n//=2
		b +=1
	return b

def d(u, p):
	return (u << (p % 5)) - 158 

def j(q,w):
	return ord(q) * 115 + ord(w) * 21

l = [-153, 462, 438, 1230, 1062, -24, -210, 54, 2694, 1254, 69, -162, 210, 150]
v = "b4f9d505"

def rec(prev, i):
	if i == len(l):
		return [""]
	val = l[i]
	possible = []
	for curr in map(chr, range(32,127)):
		if d(a(j(prev, curr) - 10), i) * 3 == val:
			possible.append(curr)
	#print(possible)
	return [poss + c for poss in possible for c in rec(poss, i + 1)]

for poss in rec("f",0):
	f = "f" + poss
	if hashlib.sha256(f.encode()).hexdigest()[:8] == v:
		print(f)
		
