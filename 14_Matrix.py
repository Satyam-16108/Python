def addM(A,B):
    result=[ [0,0,0],[0,0,0],[0,0,0] ]
    #for rows
    for i in range(len(A)):
        #for columns
        for j in range(len(A[0])):
            result[i][j]=A[i][j] + B[i][j]

    for k in result:
        print(k)

    return 0

A = [ [1,  2,  3],
      [6,  7,  4],
      [8, 10, 11] ]

B = [[1, 5, 3],
     [2, 6, 5], 
     [7, 4, 9] ]


print("Addition Result: ")
addM(A,B)

def Multiply(A,B):
    result=[ [0,0,0],[0,0,0],[0,0,0] ]
    #for rows
    for i in range(len(A)):
        #for columns
        for j in range(len(B[0])):
            #for rows of matrix B
            for k in range(len(B)):  #len(B) or len(A[0])
                result[i][j] += A[i][k] * B[k][j]

    for p in result:
        print(p)
    return 0

A = [ [1,  2,   3],
      [6,  7,   4],
      [8, 10,  11] ]

B = [[1, 5, 3],
     [2, 6, 5], 
     [7, 4, 9] ]

print("Multiplication Result: ")
Multiply(A,B)