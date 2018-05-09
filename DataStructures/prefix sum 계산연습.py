import random

def prefixSum1(x,n):
	A = [0]*n
	for i in range(n):
		#A[i]=?
		for j in range(0,i+1):
			A[i] += x[j]
	return A
	
n = int(input())
X = []
for i in range(n):
    X.append(random.randint(0,5))

X=[random.randint(0,5) for i in range(n)]

print(X)

A = prefixSum1(X,n)
print(A)
