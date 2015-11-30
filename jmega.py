import os
os.system("clear")

arq = open("mega.txt","w")

x = 1
y = 61


for a in range(x,y):
	for b in range(a+1,y):
		for c in range(b+1,y):
			for d in range(c+1,y):
				for e in range(d+1,y):
					for f in range(e+1,y):
						k = str(a)+','+str(b)+','+str(c)+','+str(d)+','+str(e)+','+str(f)+'\n'
						arq.writelines(k)
arq.close()
