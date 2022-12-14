n = int(input("Enter No. Of Items : "))
d ={}                     
for i in range(n):        
    text = input().split()     #split the input text based on space & store in the list 'text'
    d[text[0]] = text[1]       #assign the 1st item to key and 2nd item to value of the dictionary
print(d)

d = dict(map(reversed, d.items()))

print("Inverse mapped dictionary : ", str(d))