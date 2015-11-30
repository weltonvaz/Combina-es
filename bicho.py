import os
os.system("clear")

numbers = list(range(1,61))
count = 1

for x in numbers:
	for y in numbers:
		if y == x:
			continue
		for z in numbers:
			if y == x or y == z or z == x:
				continue
			count += 1
			print(count,"--> ",x,y,z)
