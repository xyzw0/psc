# Vectors
arr1 = [1,2,3]
arr2 = [4,5,6]
add=[0,0,0]
mul=[0,0,0]

for i in range(0,3):
    add[i] = arr1[i] + arr2[i]
    mul[i] = arr1[i] * arr2[i]
    
print("Addition is : " , add )
print("Multiplication is : " , mul )

""" output:
Addition is: [5, 7, 9]
Multiplication is : [4, 10, 18] """

# Matrix Addition
X = [[1,2,3], [4,5,6], [7,8,9]]
Y = [[9,8,7], [6,5,4], [3,2,1]]
result = [[0,0,0], [0,0,0], [0,0,0]]

# iterate through rows
for i in range(len(X)):
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
    
    
for r in result:
    print(r)

    [10, 10, 10]
    [10, 10, 10]
    [10, 10, 10]
    
    
# Matrix Multiplication
A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[9,8,7], [6,5,4], [3,2,1]]
result = [[0,0,0], [0,0,0], [0,0,0]]


# iterating by row of A
for i in range(len(A)):
# iterating by column by B
    for j in range(len(B[0])):
    # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]


for r in result:
    print(r)
