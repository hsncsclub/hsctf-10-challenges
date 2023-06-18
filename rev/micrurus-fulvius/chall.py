from hashlib import sha256 as k

def a(n):
	b = 0
	while n != 1:
		if n & 1:
			n *= 3
			n += 1
		else:
			n //= 2
		b += 1
	return b

def d(u, p):
	return (u << (p % 5)) - 158

def j(q, w):
	return ord(q) * 115 + ord(w) * 21

def t():
	x = input()
	l = [-153, 462, 438, 1230, 1062, -24, -210, 54, 2694, 1254, 69, -162, 210, 150]
	m = "b4f9d505"
	if len(x) - 1 != len(l):
		return False
	for i, c in enumerate(zip(x, x[1:])):
		if d(a(j(*c) - 10), i) * 3 != l[i]:
			return False
	if k(x.encode()).hexdigest()[:8] != m:
		return False
	return True

def g():
	if t():
		print("Correct")
	else:
		print("Wrong")

if __name__ == "__main__":
	g()
