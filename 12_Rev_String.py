# Function to reverse a string (using extended slice syntax)

def reverse1(string):
	string = string[::-1]
	return string

s = "keshavmahavidyalaya"

print("The original string is : ", end="")
print(s)

print("The reversed string is : ", end="")
print(reverse1(s))

# Reverse a string using reversed()

def reverse2(string):
	string = "".join(reversed(string))
	return string

s = "keshavmahavidyalaya"

print("The original string is : ", end="")
print(s)

print("The reversed string(using reversed) is : ", end="")
print(reverse2(s))

# Function to reverse a string by converting string to list then reversed it and again convert it to string

def reverse3(string):
	string = list(string)
	string.reverse()
	return "".join(string)

s = "keshavmahavidyalaya"

print("The original string is : ", s)

print("The reversed string(using reversed) is : ", reverse3(s))