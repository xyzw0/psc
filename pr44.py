# Selection Sort
def sort(num):
for i in range(5):
min = i
for j in range(i,len(num)):
if num[j]<num[min]:
min = j
temp = num[i]
num[i] = num[min]
num[min] = temp
num =[2,4,3,1,6]
sort(num)
print(num)
[1, 2, 3, 4, 6]
def mergeSort(myList):
if len(myList) > 1:
mid = len(myList) // 2
left = myList[:mid]
right = myList[mid:]
# Recursive call on each half
mergeSort(left)
mergeSort(right)
# Two iterators for traversing the two halves
i = j = 0
# Iterator for the main list
k = 0
while i < len(left) and j < len(right):
if left[i] <= right[j]:
# The value from the left half has been used
myList[k] = left[i]
# Move the iterator forward
i += 1
else:
myList[k] = right[j]
j += 1
# Move to the next slot
k += 1
# For all the remaining values
while i < len(left):
myList[k] = left[i]
i += 1
k += 1
while j < len(right):
myList[k]=right[j]
j += 1
k += 1
myList = [20,30,10,50,40]
mergeSort(myList)
print(myList)
[10, 20, 30, 40, 50]
# Tim Sort
RUN = 32
def Insertion(arr, left, right):
for i in range(left + 1, right + 1):
temp = arr[i]
j = i - 1
while arr[j] > temp and j >= left:
arr[j + 1] = arr[j]
j -= 1
arr[j + 1] = temp
def merge(arr, l, m, r):
len1, len2 = m - l + 1, r - m
left, right = [],[]
for i in range(0, len1):
left.append(arr[l + i])
for i in range(0, len2):
right.append(arr[m + 1 + i])
i, j, k = 0, 0, 1
while i < len1 and j < len2:
if left[i] <= right[j]:
arr[k] = left[i]
i += 1
else:
arr[k] = right[j]
j += 1
k += 1
while i < len1:
arr[k] = left[i]
k += 1
i += 1
while j < len2:
arr[k] = right[j]
k += 1
j += 1
S
def timSort(arr, n):
for i in range(0, n, RUN):
Insertion(arr,i,min((i + 31), (n - 1)))
size = RUN
while size < n:
for left in range(0, n, 2 * size):
mid = left + size - 1
right = min((left + 2 * size - 1),(n - 1))
merge(arr, left, mid, right)
size = 2 * size
def printArray(arr, n):
for i in range(0, n):
print(arr[i], end = " ")
print()
if __name__ == "__main__":
arr = [30,20,10,50,40]
n = len(arr)
print("The array is: ")
printArray(arr, n)
timSort(arr, n)
print("Array after sorting: ")
printArray(arr, n)
The array is: 
30 20 10 50 40 
Array after sorting: 
10 20 30 40 50 
Q44. Implement a Singly Linked List. (Insert, Display, Delete).
# Linked List
class Node:
def __init__(self, data):
self.data = data
self.next = None
class LinkedList:
def printList(self,first):
self.first = first
temp=first
while (temp):
print (temp.data)
temp = temp.next
llist = LinkedList()
first = Node(10)
second = Node(20)
third = Node(30)
first.next=second
second.next = third
llist.printList(first)
