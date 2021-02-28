def lucky_seven(A:list):
	""" Return True if sum three any elements (natural numbers)
		of list A equal 7 (seven) and print this elements; 
		else - return False.
		One element of list A can't be a summand twice.
	"""
	assert len(A) >= 3, "List must content minimum three values!"
	B = []
	# Filling tempopary list B for values less or equal 7
	B = [A[i] for i in range (len(A)) if (A[i] <= 7) and (A[i] > 0)]
	print (B)
	if len(B) < 3:
		return False
	for i in range (0, len(B)-2):
		for k in range (i+1, len(B)-1):
			for m in range (k+1, len(B)):
				if B[i] + B[k] + B[m] == 7:
					print (B[i], B[k], B[m])
					return True
	return False


A = [2, 4, 3, 8, 15, 4, 3, 5, 1]
print (lucky_seven(A))

B = [0, 5]
print (lucky_seven(B))
