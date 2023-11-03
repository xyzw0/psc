set_x={}
print("1. Create a set")
print("2. Update particular element in set")
print("3. Append to set")
print("4. Delete whole set")
print("5. Delete particular element")
print("6. Sort the set")
print("7. Find length of set")
print("8. Exit")
while True:
    ch = int(input("\nEnter choice = "))
    if ch == 1:
        set_x=set(map(int,input("Enter the elements: ").split()))
        print("Set Created:",set_x)
    elif ch == 2:
        set_y=set(map(int,input("Enter the elements: ").split()))
        set_x.update(set_y)
        print("Set after update:",set_x)
    elif ch == 3:
        y=int(input("Enter a element:"))
        set_x.add(y)
        print(set_x)
    elif ch == 4:
        if(set_x=={}):
            print("already empty")
        else:
            set_x.clear()
            print("Set Deleted")
    elif ch == 5:
        y=int(input("Enter the element :"))
        set_x.remove(y)
        print(set_x)
    elif ch == 6:
        print("Sorted set is : ", sorted(set_x))
    elif ch == 7:
        print("The length of set is:", len(set_x))
    elif ch == 8:
        print("Exit")
        break
    else:
        print("Invalid choice, Please try again")
