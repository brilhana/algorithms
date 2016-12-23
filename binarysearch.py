# Author: Alexandre Brilhante

''' Binary search. '''

def binsearch(T, x):
	if len(T) == 0 or x > T[-1]:
		return len(T)+1
	else:
		return binrec(T, x)

def binrec(T, x):
	if T[0] == T[-1]:
		return T[0]
	k = len(T)//2
	if x <= T[k]:
		return binrec(T[:k], x)
	else:
		return binrec(T[k:], x)

print(binsearch([1, 2, 3, 4, 5], 2))