fname = input("Enter file name : ") #file2.txt
fopen=open(fname,"a")
c=input("Enter string to append : ")
fopen.write(c)
fopen.close()
print("Contents of appended file : ")
file4=open(fname,'r')
line1=file4.readline()
while(line1!=""):
    print(line1)
    line1=file4.readline()
file4.close()
