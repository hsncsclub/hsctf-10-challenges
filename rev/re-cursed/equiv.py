from itertools import zip_longest

def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
	"Collect data into non-overlapping fixed-length chunks or blocks"
	# grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
	# grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
	# grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
	args = [iter(iterable)] * n
	if incomplete == 'fill':
		return zip_longest(*args, fillvalue=fillvalue)
	if incomplete == 'strict':
		return zip(*args, strict=True)
	if incomplete == 'ignore':
		return zip(*args)
	else:
		raise ValueError('Expected fill, strict, or ignore')

with open("flag.txt", "rb") as f:
	inp = f.read().strip()
autokey_out = []
prev = 57
for c in inp:
	out = prev ^ c
	autokey_out.append(out)
	prev = out

print(f"autokey: {autokey_out!r}")

transpose_out = []
for tup in grouper(reversed(autokey_out), 3):
	transpose_out.extend([tup[1], tup[2] + 3, tup[0] - 24])

print(f"transpose: {transpose_out!r}")

funny_out = [(c ^ 43) + 5 for c in transpose_out]

print(f"funny: {funny_out}")
