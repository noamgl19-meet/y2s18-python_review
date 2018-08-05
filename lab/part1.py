# Part 1 of the Python Review lab.

def hello_world():
	print("hello world")
def greet_by_name(name):
	print("hello "+str(name))

def encode(x):
	return int(x*3953531)

def decode(coded_message):
	return coded_message / 3953531
print(decode(encode(5)))