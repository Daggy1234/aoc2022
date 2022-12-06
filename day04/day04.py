lines = [[tuple([int(e) for e in d.split("-")]) for d in l.split(",")] for l in open("data.txt").readlines()]

def part_1():
	global lines
	pair_c = 0
	for l in lines:
		r_a = "." + ".".join([str(i) for i in list(range(l[0][0], l[0][1] + 1))]) + "."
		st_a = set(list(range(l[0][0], l[0][1] + 1)))
		st_b = set(list(range(l[1][0], l[1][1] + 1)))
		r_b = "." + ".".join([str(i) for i in list(range(l[1][0], l[1][1] + 1))]) + "."
		if r_a in r_b or r_b in r_a:
			pair_c += 1
	print("Part 1:")
	print(pair_c)

def part_2():
	global lines
	com_c = 0
	for l in lines:
		r_a =set(list(range(l[0][0], l[0][1] + 1)))
		r_b = set(list(range(l[1][0], l[1][1] + 1)))
		if len(r_a.intersection(r_b)) > 0:
			com_c += 1
	print("Part 2:")
	print(com_c)

part_1()
part_2()