# Write your solution for 1.4 here!

def is_prime(x):
	for i in range(1,int(x/2)):
		if x  % i != 0:
			return False
	return True
print(is_prime(8))