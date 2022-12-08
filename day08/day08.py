from typing import List


grid = [[int(a) for a in l.strip()] for l in open("data.txt","r").readlines()]

def part_1(grid: List[List[int]]):
	edge_nodes = 2 * (len(grid) -2) + len(grid[0]) * 2
	vis_tree = 0
	for i in range(1,len(grid) - 1):
		for j in range(1, len(grid[i]) - 1):
			elm = grid[i][j]
			newi = i - 1
			top_path = True
			while  newi >= 0:
				nelm = grid[newi][j]
				if nelm >= elm:
					top_path = False
					break
				newi -= 1
			if top_path:
				vis_tree += 1
				continue
			newib = i + 1
			bot_path = True
			while  newib < len(grid):
				nelm = grid[newib][j]
				if nelm >= elm:
					bot_path = False
					break
				newib += 1
			if bot_path:
				vis_tree += 1
				continue
			newj = j - 1
			lef_path = True
			while newj >= 0:
				nelm = grid[i][newj]
				if nelm >= elm:
					lef_path = False
					break
				newj -= 1
			if lef_path:
				vis_tree += 1
				continue
			newjr = j + 1
			rig_path = True
			while  newjr < len(grid[0]):
				nelm = grid[i][newjr]
				if nelm >= elm:
					rig_path = False
					break
				newjr += 1
			if rig_path:
				vis_tree += 1
				continue
	print("Part 1:")
	print(vis_tree + edge_nodes)


def part_2(grid: List[List[int]]):
	scene_scores = []
	for i in range(1,len(grid) - 1):
		for j in range(1, len(grid[i]) - 1):
			elm = grid[i][j]
			newi = i - 1
			top_path = 0
			while  newi >= 0:
				nelm = grid[newi][j]
				if nelm >= elm:
					top_path += 1
					break
				top_path += 1
				newi -= 1
			newib = i + 1
			bot_path = 0
			while  newib < len(grid):
				nelm = grid[newib][j]
				if nelm >= elm:
					bot_path += 1
					break
				bot_path += 1
				newib += 1
			newj = j - 1
			lef_path = 0
			while newj >= 0:
				nelm = grid[i][newj]
				if nelm >= elm:
					lef_path += 1
					break
				lef_path += 1
				newj -= 1
			newjr = j + 1
			rig_path = 0
			while  newjr < len(grid[0]):
				nelm = grid[i][newjr]
				if nelm >= elm:
					rig_path += 1
					break
				rig_path += 1
				newjr += 1
			scene_score = max(top_path,1) * max(bot_path,1) * max(lef_path,1) * max(rig_path,1)
			scene_scores.append(scene_score)
	print("Part 2:")
	print(max(scene_scores))
part_1(grid)
part_2(grid)