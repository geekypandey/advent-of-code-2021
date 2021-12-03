import sys

with open(sys.argv[1]) as f:
    data = f.readlines()

data = [int(d) for d in data]

count = 0
for f, s, t, four in zip(data, data[1:], data[2:], data[3:]):
    first = f+s+t
    second = s+t+four
    if second - first > 0:
        count += 1


print(count)


