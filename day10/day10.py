from typing import Tuple
import copy

instru = [l.strip().split(" ") for l in open("data.txt","r").readlines()]

def part_1(instru):
	cycle_d = {}
	cycle_c = 0
	reg_val = 1
	while len(instru) > 0:
		instuc = instru.pop(0)
		if instuc[0] == "noop":
			cycle_c += 1
			cycle_d[cycle_c] = reg_val
		else:
			cycle_c += 1
			cycle_d[cycle_c] = reg_val
			cycle_c += 1
			cycle_d[cycle_c] = reg_val
			reg_val += int(instuc[1])

	adds = [20,60,100,140,180,220]
	sig_s = 0
	for elm in adds:
		sig_s += (cycle_d[elm] * elm)
	print(sig_s)


def gen_ind(inp: int) -> Tuple[int,int]:
	if (inp > 40): return ((inp - 1)//40,inp - (40 *((inp - 1)//40)) - 1)
	return (0,inp-1)


def part_2(instru):
	cycle_d = {}
	cycle_c = 0
	reg_val = 1
	new_gri = []
	for i in range(6):
		new_gri.append(["0" for l in range(40)])
	while len(instru) > 0:
		instuc = instru.pop(0)
		if instuc[0] == "noop":
			cycle_c += 1
			r,c = gen_ind(cycle_c)
			if c in [reg_val -1, reg_val, reg_val + 1]:
				new_gri[r][c] = "#"
			else:
				new_gri[r][c] = "."
		else:
			cycle_c += 1
			r,c = gen_ind(cycle_c)
			if c in [reg_val -1, reg_val, reg_val + 1]:
				new_gri[r][c] = "#"
			else:
				new_gri[r][c] = "."
			cycle_c += 1
			r,c = gen_ind(cycle_c)
			if c in [reg_val -1, reg_val, reg_val + 1]:
				new_gri[r][c] = "#"
			else:
				new_gri[r][c] = "."
			reg_val += int(instuc[1])
	print("\n".join(["".join(l) for l in new_gri]))

	
part_1(copy.deepcopy(instru))
part_2(copy.deepcopy(instru))
