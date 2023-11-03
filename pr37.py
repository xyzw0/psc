# Initializing List
a_list=[]
even=[]
odd=[]
# Calling User Defined function
def inp(num):
    num=int(input("Enter the number : "))
    e1.a_list.append(num)
# Creating Object
e1=even_odd()
size=int(input("Enter how many numbers you want in the list : "))
# Even or odd logic
for i in range(1,size+1):
    e1.inp()
for i in e1.a_list:
    if (i % 2 == 0):
        print(i," is even ")
        e1.even.append(i)
    else:
        print(i," is odd ")
        e1.odd.append(i)
    # Printing the Even List and Odd List
print(e1.even)
print(e1.odd)
print('Total number of even = ', len(e1.even))
print('Total number of even = ', len(e1.odd))
