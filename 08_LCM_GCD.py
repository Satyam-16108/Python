"""# Recursive function to return gcd of a and b
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
# Function to return LCM of two numbers
def lcm(a,b):
    return (a / gcd(a,b))* b
 
# Driver program
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))"""



# Function to find gcd of two numbers
def gcd(a, b):
  # Find minimum of a and b
  result = min(a, b)
   
  while result:
    if a % result == 0 and b % result == 0:
      break
    result -= 1
   
  # Return the gcd of a and b
  return result

# Function to find LCM of two numbers
def LCM(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           Lcm = greater
           break
       greater += 1

   return Lcm

a = 48
b = 24
print('LCM of', a, 'and', b, 'is', LCM(a, b))

if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')