def getSum(n):
    sum = 0
    while (n != 0):
      sum += int(n % 10)
      n = n//10
    return sum

n = int(input("ENTER A NUMBER : "))
rev = int(0) 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print("Reverse Of Digits : ",rev)
print("Sum Of Digits : ",getSum(rev))