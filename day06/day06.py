inp = open("data.txt","r").readlines()[0].strip()

def proc_fun(num_to_check: int):
	for i in range(0,len(inp)-(num_to_check-1)):
		if len(set(inp[i:i+num_to_check])) >= num_to_check:
			print(i+num_to_check)
			break
def part_1():
	print("Part 1:")
	proc_fun(4)

def part_2():
	print("Part 2:")
	proc_fun(11)

part_1()
part_2()