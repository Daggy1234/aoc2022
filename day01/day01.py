lines = [l.strip() for l in open("data.txt").readlines()]

summer = 0
vals = []
for val in lines:
    if val != '':
        summer += int(val)
    else:
        vals.append(summer)
        summer = 0

print("Part 1:")
print(max(vals))

vals.sort(reverse=True)
max_sum = 0
for i in range(3):
    max_sum += vals[i]
print("Part 2:")
print(max_sum)
