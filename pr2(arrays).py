arr = [2,5,10,'Peter']
arr.append(7)
print("After inserting : " , arr)
arr.remove(10)
print("After removing : " , arr)

arr1 = [1,2,3]
arr2 = [4,5,6]
add=[0,0,0]
sub=[0,0,0]
mult=[0,0,0]
div=[0,0,0]
mod=[0,0,0]

for i in range(0,3):
    add[i] = arr1[i] + arr2[i]
    sub[i] = arr1[i] - arr2[i]
    mult[i]= arr1[i] * arr2[i]
    mod[i] = arr1[i] % arr2[i]
    div[i] = arr1[i] / arr2[i]
    
    
print('The Answers are :- ')
print("Addition is : " , add )
print("Subtraction is : " , sub )
print("Multiplication is : " , mult )
print("Division is : " , div )
print("Modulo is : " , mod )
