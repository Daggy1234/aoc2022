inp = open("data.txt","r").readlines()[0].strip()

for i in range(0,len(inp)-13):
	if len(set(inp[i:i+14])) >= 14:
		print(i+14)
		break