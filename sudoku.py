import sys

def lire_fichier(textfile):
	f=open(textfile,'r')
	next(f)
	i=0
	j=0
	matrice=[[0 for x in range(9)] for y in range(9)]
	#print(matrice)
	while True:
		j=0
		char=f.readline()
		for c in char:
			matrice[i][j]=int(c)
			#print(i,j)
			j=j+1
			if j==9:
				i=i+1
				break
		if i==9:
			break
	return matrice

def check_soduku(ligne,colonne,num,table_de_matrice):
	check=0
	for i in range(0,9):
		if table_de_matrice[ligne][i]==num:
			check=1
	for i in range(0,9):
		if table_de_matrice[i][colonne]==num:
			check=1
	ligne=ligne-ligne%3
	colonne=colonne-colonne%3

	for i in range(0,3):
		for j in range(0,3):
			if table_de_matrice[ligne+i][colonne+j]==num:
				check=1
	if check==1:
		return False
	else:
		return True

class calls:
	num_de_calls=0
c = calls()
def solveur_sudoku(matrice):
	c.num_de_calls=c.num_de_calls+1
	break_condition=0
	for i in range(0,9):
		for j in range(0,9):
			if matrice[i][j]==0:
				break_condition=1
				ligne=i
				colonne=j
				break
	
	#print(break_condition)
	if break_condition==0:
		print("Solution basique et moins performante : ")
		for i in matrice:
			print(i)
		print("Nombre de recursions :")
		print(c.num_de_calls)
		exit(0)

	#print("hello")
	for i in range(0,10):
		if check_soduku(ligne,colonne,i,matrice):
			matrice[ligne][colonne]=i
			if solveur_sudoku(matrice):
				return True
			matrice[ligne][colonne]=0
	return False

matrice=lire_fichier(sys.argv[1])
solveur_sudoku(matrice)

print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''matrice'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(matrice)
