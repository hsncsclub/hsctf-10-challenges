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

funny_out = [
	39, 91, 124, 92, 61, 51, 7, 105, 122, 106, 19, 41, 56, 75, 83, 132, 6, -35, 14, 105, 5, 106, 24,
	37, 29, 78, 22
]

print(f"funny: {funny_out}")

transpose_out = [(c - 5) ^ 43 for c in funny_out]

print(f"transpose: {transpose_out!r}")

autokey_out: list[int] = []
for tup in grouper(transpose_out, 3):
	autokey_out.extend([tup[2] + 24, tup[0], tup[1] - 3])

autokey_out.reverse()

print(f"autokey: {autokey_out!r}")

keystream = [57] + autokey_out
inp = [c ^ d for c, d in zip(keystream, autokey_out)]

print(bytes(inp).decode())