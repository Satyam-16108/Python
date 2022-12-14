def pattern_1(n):
  for i in range (0,n):
     for j in range(0,n-i):
         print(" ",end="")

     for j in range(0,2*i-1):
         print("*",end="")
     print()
     
  for i in range (n,0,-1):
     for j in range(n-i,0,-1):
         print(" ",end="")

     for j in range(2*i-1,0,-1):
         print("*",end="")
     print()

     
def pattern_2(n):
 count = 1
 for i in range (0,n+1):
     for j in range(0,n-i):
         print(" ",end="")

     for j in range(0,i):
         print(count,end="")
         count+=1

     for j in range(0,i-1):
         print(count-2,end="")
         count-=1
     print()

n=int(input("ENTER NO OF ROWS : "))
pattern_1(n)
pattern_2(n)
