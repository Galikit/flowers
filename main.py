d = {}
with open("iris.data", "r") as file:
    for line in file:
        if not line.strip():
            continue
        line = line.strip().split(",")
        if not line[4] in d:
            d[line[4]] = 0
        d[line[4]] += float(line[3])

d1, d2, d3 = [{k: v} for k, v in d.items()]

for dx in d1, d2, d3:
    for k, v in dx.items():
        print(k, str(v))
