'''
Name : Ratnesh Chandak
Roll No: CS12B1030
Btech 4th year
file : program of RREF
Note : please read instruction to run the program from readme
'''
import os

def interchange(M,i,j):
    M[i],M[j] = M[j],M[i]

def divide(A,k):
	for j in range(len(A)):
		A[j]/=float(k)

def sub(A,B):
	for j in range(len(A)):
		A[j]-=B[j]

def mult(A,k):
	for j in range(len(A)):
		A[j]*=float(k)

M=[]
#getting input
f = open(os.getcwd()+'/input1.txt', 'r')
for line in f:
        C=[]
        line=line.split(",")
        for word in line:
        	C.append(float(word))
        M.append(C)

f.close()
print "input :"
print M

rows = len(M)
columns = len(M[0])

#making the starting element in each row = 1
for i in range(rows):
	pivot=0
	for j in range(columns):
		if(M[i][j]!=0):
			pivot=M[i][j]
	if(pivot!=0):
		divide(M[i],pivot)

for i in range(min(columns,rows)):
	j=i
	pivot=M[i][j]
	r=i+1
	while(pivot==0 and r<rows):
		interchange(M,i,r)
		pivot=M[i][j]
		r+=1
		
	if(pivot!=0):
		divide(M[i],pivot)
	
	#making the ith column of rows from i+1 onwards as 0
	for p in range(i+1,rows):
		A = []
		for t in range(columns):
			A.append(M[i][t])
		mult(A,M[p][j])
		sub(M[p],A)

s=0
if(columns <= rows ):
		s=columns -1
else:
	s=rows

#creating identity matrix in the sub matrix
for i in range(rows):
	for j in range(i+1,s):
		A = []
		for t in range(columns):
			A.append(M[j][t])
		mult(A,M[i][j])
		sub(M[i],A)

print "output : "
for i in range(rows):
	print M[i]

#output to the file
f=open(os.getcwd()+'/output.txt', 'w')
for i in range(rows):
	for j in range(columns):
		f.write(str(round(M[i][j],2)))
		if(j<columns-1):
			f.write(",")
	f.write('\n')

rank=0
s=min(columns,rows)
for i in range(rows):
	j=i
	while(j < s and M[i][j]==0 ):
		j+=1
	if(j < columns and M[i][j]!=0):
		rank+=1	
print "the rank of the matrix is:"
print rank

f.write("the rank of the matrix is ")
f.write(str(rank))
f.write(". ")

if(rank == columns-1):
	check=0
	for j in range(columns-1):
			if(M[rank-1][j]!=0):
				check=1
	if(check==1):
		print " The system of equation has unique solution ",
		print "("
		f.write(" The system of equation has unique solution.")
		f.write("(")
		for i in range(rows):
			print round(M[i][columns-1],2),
			f.write(str(round(M[i][columns-1],2)))
			if(i!=rows-1):
				print ","
				f.write(",")
		print ")"
		f.write(")")
		f.close()
	else:
		print " The system of equation has no solution"
		f.write( " The system of equation has no solution")
		f.close()

elif(rank < columns-1):
	print " The system of equation has infinite solution with described by an affine subspace of dimension "
	print columns -1 - rank
	f.write(" The system of equation has infinite solution with described by an affine subspace of dimension ");
	f.write(str(columns -1 - rank))
	f.write(". ")
	f.close()

else:
	print " The system of equation has no solution"
	f.write( " The system of equation has no solution")
	f.close()