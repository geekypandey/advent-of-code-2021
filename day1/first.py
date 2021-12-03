import sys

with open(sys.argv[1]) as f:
    data = f.readlines()


prev = None
count = 0
for d in data:
    d = int(d)
    if prev is not None and d - prev > 0:
        count += 1
    prev = d

print(count)


