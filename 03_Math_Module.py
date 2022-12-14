import math
a = 2.3
b = 5
c = 30
d = -10
e = math.pi/6

# Print the value of Euler e
print (math.e)
# Print the value of pi
print (math.pi)
# Print the value of tau
print (math.tau)
# Print the value of tau
print (math.tau)
# Print the value of nan
print (math.nan)
# Print the factorial
print("The factorial of 5 is : ", end="")
print(math.factorial(b))
# Print the GCD
print (math.gcd(c, b))
# Print the absolute value
print ("The absolute value of -10 is : ", end="")
print (math.fabs(d))
# Power
print (pow(3,4))
# Square Root
print(math.sqrt(4))

# Ceil of 2.3
print ("The ceil of 2.3 is : ", end="")
print (math.ceil(a))
 # Floor of 2.3
print ("The floor of 2.3 is : ", end="")
print (math.floor(a))

# exp() Values
test_int = 4
test_neg_int = -3
test_float = 0.00
print (math.exp(test_int))
print (math.exp(test_neg_int))
print (math.exp(test_float))

# LOG Function
print ("The value of log 2 with base 3 is : ", end="")
print (math.log(2,3))
print ("The value of log2 of 16 is : ", end="")
print (math.log2(16))
print ("The value of log10 of 10000 is : ", end="")
print (math.log10(10000))

# sin(), cos(), tan()
print ("The value of sine of pi/6 is : ", end="")
print (math.sin(a))
print ("The value of cosine of pi/6 is : ", end="")
print (math.cos(a))
print ("The value of tangent of pi/6 is : ", end="")
print (math.tan(a))

# Radians And Degrees
print ("The converted value from radians to degrees is : ", end="")
print (math.degrees(e))
print ("The converted value from degrees to radians is : ", end="")
print (math.radians(c))

# Checking if Infinity
print ("Pie is Infinity : ",math.isinf(math.pi))
print ("Exponent e is Infinity : ",math.isinf(math.e))
print ("Infinity is Infinity : ",math.isinf(float('inf')))

# Printing the gamma value
print ("The gamma value  is : ",str(math.gamma(b)))