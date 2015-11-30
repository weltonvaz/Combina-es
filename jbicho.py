import os
os.system("clear")

import itertools

lista = list(range(1,60))
jbicho = list(itertools.permutations(lista, 6))

arq = open("mega.txt","w")
for j in jbicho:
	k = str(j)
	arq.writelines(k+'\n')
arq.close()
