# Part 2 of the Python Review lab.

def is_prime(x):
	for i in range(2,int(x)):
		if int(x) % i == 0:
			print("not a prime")
			x = input("re enter x please")
			is_prime = True
			i = x
			break
		else:
			is_prime = True
	return is_prime

def encode(x, y):
	if (int(x) < 500 or int(x) > 1000 or int(y) < 1 or int(y) > 250):
		print("Invalid input: Outside range")
		return "None"
	# check p[rime]	
	if is_prime(x):	
		print("congrats, this number is a prime number")
		num = x*y
	else:
		encode(x,y)

def decode(coded_message):
	pass
encode(500,6)