from math import sqrt

n = int(input("ENTER A NUMBER : "))

# this flag maintains status whether the n is prime or not
prime_flag = 0

if(n > 1):
	for i in range(2, int(sqrt(n)) + 1):
		if (n % i == 0):
			prime_flag = 1
			break
	if (prime_flag == 0):
		print(n,"IS PRIME")
	else:
		print(n,"IS NOT PRIME")
else:
	print(n,"IS NOT PRIME")
