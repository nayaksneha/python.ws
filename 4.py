def is_prime(N):
	if N<2:
		return False
	else:
		for i in range(2,N//2+1): 
			if N%i == 0:
				return False
		return True

LB = int(input("enter lower bond"))
UB = int(input("enter upper bond"))
for i in range(LB,UB+1):
	if is_prime(i):
		print(i)