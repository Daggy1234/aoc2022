ops = [l.strip().split(" ") for l in open("data.txt", "r").readlines()]
ss = 0
scores = {'X': 1, 'Y': 2, 'Z': 3}
for i in ops:
	if (i[0] == 'A' and i[1] == 'Y') or (i[0] == 'B' and i[1] == 'Z') or (i[0] == 'C' and i[1] == 'X'):
		ss += 6
		ss += scores[i[1]]
	elif (i[0] == 'A' and i[1] == 'Z') or (i[0] == 'B' and i[1] == 'X') or (i[0] == 'C' and i[1] == 'Y'):
		ss += 0
		ss += scores[i[1]]
	else:
		ss += 3
		ss += scores[i[1]]

sst = 0
draw_map = {
	'A': 1,
	'B': 2,
	'C': 3,
}
win_map = {
	'A': 2,
	'B': 3,
	'C': 1,
}
loss_map = {
	'A': 3,
	'B': 1,
	'C': 2,
}
for i in ops:
	if i[1] == 'X':
		sst += 0
		sst += loss_map[i[0]]
	elif i[1] == 'Y':
		sst += 3
		sst += draw_map[i[0]]
	else:
		sst += 6
		sst += win_map[i[0]]

print("Part 1:")
print(ss)
print("Part 2:")
print(sst)

