import json

from utils.rng.java_random import JavaRandom, find_seed_long

with open("out.txt") as f:
	ct = json.load(f)
known = bytes.fromhex("89 50 4e 47 0d 0a 1a 0a")
k = (
	(known[0] << 56) + (known[1] << 48) + (known[2] << 40) + (known[3] << 32) + (known[4] << 24) +
	(known[5] << 16) + (known[6] << 8) + (known[7])
) - (1 << 64)
l = k ^ ct[0]

seed = find_seed_long(l)
rand = JavaRandom(seed)
pt = [(k + (1 << 64)).to_bytes(8, "big")]
for c in ct[1:]:
	r = rand.next_long()
	p = c ^ r
	if p < 0:
		p += 1 << 64
	pt.append(p.to_bytes(8, "big"))

with open("out.png", "wb") as f:
	f.write(b"".join(pt))
