f1 = input("Enter file-1 name : ")
fin=open(f1,'w')
data1=input("Enter data in file1 : ")
fin.write(data1)
fin.close()
f2 = input("Enter file-2 name : ")
fout = open(f2, "a")
data2=input("Enter data in file2 : ")
data=data1+data2
fout.write(data)
fout.close()
fout=open(f2,'r')
text=fout.read()
print(text)
print("\nFile content appended successfully")
