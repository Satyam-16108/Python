def Series1(x, n):
    sum = 1
    term = 1
    fct = 1
    p = 1
    mul = 1
     
    for i in range(1, n):
        fct = fct * mul * (mul+1)
        p = p*x*x
        term = (-1) * term
        mul += 2
        sum = sum + (term * p)/fct
     
    return sum
 
def Series2(x, n):
    sum = 1
    term = 1
    fct = 1
    p = 1
    mul = 1
     
    for i in range(1, n):
        fct = fct * mul * (mul+1)
        p = p*x*x
        mul += 2
        sum = sum + (p)/fct
     
    return sum
    
# DRIVER CODE
print("(i) 1 - x^2/2! + x^4/4! - …. upto nth term")
print("(ii) 1 + x^2/2! + x^4/4! + …. upto nth term") 
x= int(input("ENTER Value Of x : "))
n= int(input("ENTER Value Of n : "))
print("(i) Sum Of Series - ", '%.4f'% Series1(x, n))
print("(ii) Sum Of Series - ", '%.4f'% Series2(x, n))
# '%.4f'% -> to limit decimal value to 4 digits