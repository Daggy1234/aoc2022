import string
from typing import Dict, List, Tuple
from collections import deque

filename = "data.txt"

def part_1():
	global filename
	elv_d = {}
	for i,char in enumerate("S" + string.ascii_lowercase+"E"):
		elv_d[char] = i+1

	gri_t = [[c for c in l.strip()] for l in open(filename).readlines()]
	ngrid = {}
	grid: Dict[Tuple[int,int],List[Tuple[int,int]]] = {}
	start_c = None
	goal_c = None

	for i in range(len(gri_t)):
		for j in range(len(gri_t[0])):
			if gri_t[i][j] == "E":
				goal_c = (i,j)
				ngrid[(i,j)] = elv_d[gri_t[i][j]]
			elif gri_t[i][j] == "S":
				start_c = (i,j)
				ngrid[(i,j)] = elv_d[gri_t[i][j]]
			else:
				ngrid[(i,j)] = elv_d[gri_t[i][j]]
			grid[(i,j)] = []


	for i in range(len(gri_t)):
		for j in range(len(gri_t[0])):
			itm = ngrid[(i,j)]
			if v := ngrid.get((i+1,j)):
				if (v <= (itm + 1)):
					grid[(i,j)].append((i+1,j))
			if (v := ngrid.get((i-1,j))):
				if (v <= (itm + 1)):
					grid[(i,j)].append((i-1,j))
			if (v := ngrid.get((i,j+1))):
				if (v <= (itm + 1)):
					grid[(i,j)].append((i,j+1))
			if (v := ngrid.get((i,j-1))):
				if (v <= (itm + 1)):
					grid[(i,j)].append((i,j-1))


	dist_map = {}
	queue = deque()
	queue.append((0,start_c))
	while len(queue) > 0:
		d,itm = queue.popleft()
		if itm in dist_map:
			continue
		dist_map[itm] = d
		for neighbor in grid[itm]:
			if neighbor == goal_c:
				print(d+1)
				break
			queue.append((d+1,neighbor))

def part_2():
	global filename
	elv_d = {}
	for i,char in enumerate("S" + string.ascii_lowercase+"E"):
		elv_d[char] = i+1

	gri_t = [[c for c in l.strip()] for l in open(filename).readlines()]
	ngrid = {}
	grid: Dict[Tuple[int,int],List[Tuple[int,int]]] = {}
	start_c = []
	goal_c = None

	for i in range(len(gri_t)):
		for j in range(len(gri_t[0])):
			if gri_t[i][j] == "E":
				goal_c = (i,j)
				ngrid[(i,j)] = elv_d[gri_t[i][j]]
			elif gri_t[i][j] == "S" or gri_t[i][j] == "a":
				start_c.append((i,j))
				ngrid[(i,j)] = elv_d[gri_t[i][j]]
			else:
				ngrid[(i,j)] = elv_d[gri_t[i][j]]
			grid[(i,j)] = []


	for i in range(len(gri_t)):
		for j in range(len(gri_t[0])):
			itm = ngrid[(i,j)]
			if v := ngrid.get((i+1,j)):
				if (v <= (itm + 1)):
					grid[(i,j)].append((i+1,j))
			if (v := ngrid.get((i-1,j))):
				if (v <= (itm + 1)):
					grid[(i,j)].append((i-1,j))
			if (v := ngrid.get((i,j+1))):
				if (v <= (itm + 1)):
					grid[(i,j)].append((i,j+1))
			if (v := ngrid.get((i,j-1))):
				if (v <= (itm + 1)):
					grid[(i,j)].append((i,j-1))


	dist_map = {}
	queue = deque()
	for c in start_c:
		queue.append((0,c))
	while len(queue) > 0:
		d,itm = queue.popleft()
		if itm in dist_map:
			continue
		dist_map[itm] = d
		for neighbor in grid[itm]:
			if neighbor == goal_c:
				print(d+1)
				break
			queue.append((d+1,neighbor))

print("Part 1:")
part_1()
print("Part 2:")
part_2()



