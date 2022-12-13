from typing import List, Tuple


class Monkey:
	def __init__(self, inp: List[str]) -> None:
		self.itms: List[int] = [int(n) for n in inp[1].split(":")[1].strip().split(", ")]
		self.instu: str = inp[2].split("=")[1].strip()
		self.cond: int = int(inp[3].split(" ")[-1])
		self.ctr = 0
		self.true_m: int = int(inp[4].split(" ")[-1])
		self.fall_m: int = int(inp[5].split(" ")[-1])

	def __str__(self) -> str:
		return f"<Monkey instu='{self.instu}' acitivity={self.ctr} condition={self.cond} true_monkey={self.true_m} fail_monkey={self.fall_m}>"

	def run_op(self):
		self.itms = [eval(self.instu) for old in self.itms]
		self.ctr += len(self.itms)
		# print(self.itms)

	def run_bored(self):
		self.itms = [old//3 for old in self.itms]

	def run_check(self) -> Tuple[Tuple[int,List[int]], Tuple[int,List[int]]]:
		t_itms = [l for l in self.itms if ((l % self.cond) == 0)]
		f_itms = [l for l in self.itms if ((l % self.cond) != 0)]
		self.itms = []
		return ((self.true_m, t_itms), (self.fall_m,f_itms))

	def get_throw(self, inp: List[int]):
		self.itms.extend(inp)


class MonkeyGame:
	def __init__(self, inp: List[Monkey]) -> None:
		self.monkey_l: List[Monkey] = inp

	def run_round(self):
		for monk in self.monkey_l:
			monk.run_op()
			monk.run_bored()
			true_cs, fall_cs = monk.run_check()
			self.monkey_l[true_cs[0]].get_throw(true_cs[1])
			self.monkey_l[fall_cs[0]].get_throw(fall_cs[1])
	
	def run_round_pt2(self):
		for monk in self.monkey_l:
			monk.run_op()
			true_cs, fall_cs = monk.run_check()
			self.monkey_l[true_cs[0]].get_throw(true_cs[1])
			self.monkey_l[fall_cs[0]].get_throw(fall_cs[1])

	def run_counts(self):
		arr = [m.ctr for m in self.monkey_l]
		arr.sort(reverse=True)
		print(arr[0] * arr[1])


ll = [f.strip() for f in open("test_data.txt","r").readlines() if (f.strip() != "")]
def part_1():
	monkey_l = []
	for i in range(0,len(ll), 6):
		em = Monkey(ll[i:i+6])
		monkey_l.append(em)
	game = MonkeyGame(monkey_l)

	for j in range(20):
		game.run_round()

	game.run_counts()

def part_2():
	monkey_l = []
	for i in range(0,len(ll), 6):
		em = Monkey(ll[i:i+6])
		monkey_l.append(em)
	game = MonkeyGame(monkey_l)

	for j in range(20):
		game.run_round_pt2()

	game.run_counts()

print("Part 1:")
part_1()
print("Part 2:")
part_2()

