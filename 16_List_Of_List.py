def table(num):
    for i in range(1,num+1,1):
        list[i-1][0]=f'{i} X 1 = {i*1}'
        list[i-1][1]=f'{i} X 2 = {i*2}'
        list[i-1][2]=f'{i} X 3 = {i*3}'
        list[i-1][3]=f'{i} X 4 = {i*4}'
        list[i-1][4]=f'{i} X 5 = {i*5}'
        
num=int(input("Enter a number : "))
list=[[[] for i in range(5)] for i in range(num)]
table(num)
for i in range (num):
    print(list[i])