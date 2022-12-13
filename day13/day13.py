import functools
from typing import Union


l = [l.strip() for l in open("data.txt").readlines() if (l.strip() != "")]




def recursive_compare(left_side, right_side):
	# print(left_side, right_side)
	if isinstance(left_side, list) and isinstance(right_side, list):
		m = min(len(left_side), len(right_side))
		for i in range(m):
			o = recursive_compare(left_side[i],right_side[i])
			if o != None:
				return o
		if len(left_side) == len(right_side):
			return None
		return len(right_side) > len(left_side)
	if isinstance(left_side, int) and isinstance(right_side, int):
		if left_side == right_side:
			return None
		return right_side > left_side
	if isinstance(left_side, list) and isinstance(right_side, int):
		return recursive_compare(left_side, [right_side])
	if isinstance(left_side, int) and isinstance(right_side, list):
		return recursive_compare([left_side], right_side)
	raise Exception("WTF")


def compare_func(itm_a, itm_b):
	o = recursive_compare(itm_a, itm_b)
	if o:
		return 1
	return -1



def part_1():
	tup_l = []
	for i in range(0,len(l), 2):
		tup_l.append((eval(l[i]), eval(l[i+1])))
	summer = 0
	for i in range(len(tup_l)):
		o = recursive_compare(tup_l[i][0], tup_l[i][1])
		if o:
			summer += (i+1)
	print(summer)

def part_2():
	a = [[2]]
	b = [[6]]
	data = [eval(l) for l in l] + [a] + [b]
	data.sort(key=functools.cmp_to_key(compare_func),reverse=True)
	print((data.index(a)+1) * (data.index(b) + 1))

print("Part 1:")
part_1()
print("Part 2:")
part_2()