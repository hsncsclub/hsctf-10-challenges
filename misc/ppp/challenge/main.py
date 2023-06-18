#!/usr/bin/env python3
import json
with open("locations.json") as f:
	locations = json.load(f)
wrong = False
for i, coords in enumerate(locations, start=1):
	x2, y2 = coords
	x, y = map(float, input(f"Location {i}: ").split(" "))
	if abs(x2 - x) < 0.002 and abs(y2 - y) < 0.002:
		print("Correct!")
	else:
		print("Wrong!")
		wrong = True

if not wrong:
	with open("flag.txt") as f:
		print(f.read().strip())
