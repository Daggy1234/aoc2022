from collections import deque
from typing import List

def main_func(part_2: bool):
	lines = [l for l in open("data.txt").readlines()]
	lines_p = [l.strip() for l in lines]
	f_l = None
	ind = 0
	for ind in range(len(lines_p)):
		if not lines_p[ind].startswith("["):
			f_l = lines_p[ind]
			break
	stack_data = lines[:ind]
	indtructions = lines_p[ind+2:]
	if not f_l:
		raise Exception("oops")
	nums = [int(i) for i in f_l.split("   ")]
	max_n = max(nums)
	stack_arr: List[deque] = []
	for i in range(max_n):
		stack_arr.append(deque())
	stack_data.reverse()
	for bitty in stack_data:
		bitty = bitty.replace("\n","")
		new_l = []
		for char in range(1,len(bitty), 4):
			new_l.append(bitty[char])
		for i in range(len(new_l)):
			if new_l[i] != " ":
				stack_arr[i].append(new_l[i])
	parsed_instru = [[int(v) for v in intro.split(" ")[1::2]] for intro in indtructions]
	for instru in parsed_instru:
		itms = instru[0]
		from_ind = instru[1] - 1
		to_ind = instru[2] - 1
		temp_stack = []
		for i in range(itms):
			it = stack_arr[from_ind].pop()
			temp_stack.append(it)
		if part_2:
			temp_stack.reverse()
		for itm in temp_stack:
			stack_arr[to_ind].append(itm)
	t_str_l = []
	for stack in stack_arr:
		if len(stack) > 0:
			t_str_l.append(stack.pop())
		else:
			t_str_l.append(" ")
	print("".join(t_str_l))


def part_1():
	print("Part 1:")
	main_func(False)

def part_2():
	print("Part 2:")
	main_func(True)

part_1()
part_2()