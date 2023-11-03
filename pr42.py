#linear search
l1=[10,20,30,40,50]
def linear_search():
num=int(input("Enter the number to search: "))
if num in l1:
for i in range(0,len(l1)):
if l1[i]==num:
print("It is at index: ",i)
else:
print("element not present")
linear_search()
Enter the number to search: 30
It is at index: 2
# BINARY SEARCH
pos=-1
def search(list,key):
left = 0
right = len(list)-1
while left<=right:
mid = (left + right) // 2
if list[mid] == key:
globals() ["pos"] = mid
return True
else:
if list[mid]< key:
left = mid
else:
right = mid
list=[2,3,4,5,6]
key=3
if(search(list,key)):
print('Element Found at', pos )
else:
print('Element Not Found')
Element Found at 1