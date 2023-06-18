import hashlib

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
	with open("flag.txt") as f:
		x = f.read()
	l = []
	for i, c in enumerate(zip(x, x[1:])):
		l.append(d(a(j(*c) - 10), i) * 3)
	print(l)
	print(hashlib.sha256(x.encode()).hexdigest()[:8])

if __name__ == "__main__":
	t()