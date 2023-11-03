list1 = []
print("1. Create a list")
print("2. Update element in list")
print("3. Append to list")
print("4. Delete whole list")
print("5. Delete particular element")
print("6. Sort the list")
print("7. Find length of list")
print("8. Exit")
while True:
    ch = int(input("\nEnter choice = "))

    if ch == 1:
        print("Enter the elements: ")
        list1=list(map(int,input().split()))
        print("List Created:",list1)
    elif ch == 2:
        loc,val=map(int,input("Enter index and value: ").split())
        list1[loc]=val
        print("List after update:",list1)
    elif ch == 3:
        val = int(input("Enter an element to be appended: "))
        list1.append(val)
        print("List after append:", list1)
    elif ch == 4:
        list1.clear()
        print("List deleted successfully")
        print(list1)
    elif ch == 5:
        val = int(input("Enter an element want to delete: "))
        list1.remove(val)
        print("List after deletion:", list1)
    elif ch == 6:
        list1.sort()
        print("List in ascending order:",list1)
        list1.sort(reverse=True)
        print("List in descending order:",list1)
    elif ch == 7:
        print("Length of list:",len(list1))
    elif ch == 8:
        print("Exit")
        break

else:
    print("Invalid choice, Please try again")
