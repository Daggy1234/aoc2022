import string

i = 1
priorities = {}
for char in string.ascii_lowercase:
	priorities[char] = i
	i+=1
for char in string.ascii_uppercase:
	priorities[char] = i
	i+=1
print(priorities)

def part_a():
	lines = [line.strip() for line in open("data.txt", "r").readlines()]
	uncommon = []
	for l in lines:
		l_l = len(l) // 2
		part_a = set(list(l[:l_l]))
		part_b = set(list(l[l_l:]))
		elemnts = list(part_a.intersection(part_b))
		uncommon.extend(elemnts)

	score = 0
	for item in uncommon:
		score += priorities[item]
	print(score)

def part_b():
	lines = [line.strip() for line in open("data.txt", "r").readlines()]
	badges = []
	for i in range(0,len(lines),3):
		elms = lines[i:i+3]
		itms = []
		for j in range(len(elms)):
			itms.append(set(list(elms[j])))
		set_a = itms[0].intersection(itms[1])
		set_b = set_a.intersection(itms[2])
		badges.extend(list(set_b))

	print("Part 2:")
	score = 0
	for item in badges:
		score += priorities[item]
	print(score)

part_b()
