import sys

with open(sys.argv[1]) as f:
    data = f.readlines()
    data = [int(d) for d in data]

count = sum(True for f, s in zip(data, data[3:]) if s - f > 0)

print(count)


