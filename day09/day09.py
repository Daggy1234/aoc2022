import copy
bc = [l.strip().split(" ") for l in open("test_data.txt","r").readlines()]
max_dims = max([int(a[1]) for a in bc]) + 1
grid = [["." for j in range(max_dims)] for i in range(max_dims)]
grid_h = [0,len(grid) - 1]
grid_t = [0, len(grid) - 1]
visited_nodes = []
visited_nodes.append((grid_t[0], grid_t[1]))
print(len(grid))

def print_grid():
	print("=" * 10)
	new_grid = copy.deepcopy(grid)
	new_grid[grid_t[1]][grid_t[0]] = "T"
	new_grid[grid_h[1]][grid_h[0]] = "H"
	print("\n".join(["".join(g) for g in new_grid]))

print_grid()

for instruction in bc:
	dire = instruction[0]
	direi = int(instruction[1])
	print(grid_h)
	print(instruction)
	match dire:
		case "R":
			if direi == 1:
				grid_h[0] += direi
			else:
				if grid_t[1] == grid_h[1]:
					grid_h[0] += direi
					for ch in range(direi):
						visited_nodes.append((grid_t[0] + ch, grid_t[1]))
					grid_t[0] += (direi - 1)
				
				else:
					grid_h[0] += direi
					grid_t[1] = grid_h[1]
					for ch in range(1,direi):
						visited_nodes.append((grid_t[0] + ch, grid_t[1]))
					grid_t[0] += (direi - 1)
		case "L":
			if direi == 1:
				grid_h[0] -= direi
			else:
				if grid_t[1] == grid_h[1]:
					grid_h[0] -= direi
					for ch in range(direi):
						visited_nodes.append((grid_t[0] - ch, grid_t[1]))
					grid_t[0] -= (direi - 1)
				else:
					grid_h[0] -= direi
					grid_t[1] = grid_h[1]
					for ch in range(1,direi):
						visited_nodes.append((grid_t[0] - ch, grid_t[1]))
					grid_t[0] -= (direi - 1)
		case "U":
			if direi == 1:
				grid_h[1] -= direi
			else:
				if grid_t[0] == grid_h[0]:
					grid_h[1] -= direi
					for ch in range(direi):
						visited_nodes.append((grid_t[0], grid_t[1] - ch))
					grid_t[1] -= (direi - 1)
				else:
					grid_h[1] -= direi
					grid_t[0] = grid_h[0]
					for ch in range(1,direi):
						visited_nodes.append((grid_t[0], grid_t[1] - ch))
					grid_t[1] -= (direi - 1)

		case "D":
			if direi == 1:
				grid_h[1] += direi
			else:
				if grid_t[0] == grid_h[0]:
					grid_h[1] += direi
					for ch in range(direi):
						visited_nodes.append((grid_t[0], grid_t[1] + ch))
					grid_t[1] += (direi - 1)
				else:
					grid_h[1] += direi
					grid_t[0] = grid_h[0]
					for ch in range(1,direi):
						visited_nodes.append((grid_t[0], grid_t[1] - ch))
					grid_t[1] += (direi - 1)

	print_grid()

print(visited_nodes)
fs = (set(visited_nodes))
print("=" * 10)
new_grid = copy.deepcopy(grid)
for cord in fs:
	new_grid[cord[1]][cord[0]] = "#"
print("\n".join(["".join(g) for g in new_grid]))
