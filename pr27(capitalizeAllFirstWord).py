# Create a file
fname = input("Enter file name: ") #cap.txt
# Enter data in file
fopen=open(fname,'w')
fopen.write("hello")
fopen.close()
# Capitalize Every first Letter
fopen = open('cap.txt', 'r')
for line in fopen:
    output = line.title()
    print(output)