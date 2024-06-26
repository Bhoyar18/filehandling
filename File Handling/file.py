
# Files: 1. text file
#        2. binary file - audio,video
#        3. CSV

 


# f1=open("file1.txt","w")
# f1.write("File Handling day 1")
# f1.close()
# f1=open("file1.txt","a")
# f1.write("\nFile Handling in python to store data and code ")
# f1.close()

# f1=open("file2.txt","w")
# f1.write("File handling is required for python to store code")
# f1.close()
# f1=open("file2.txt","a")
# f1.write("\nFile Handling in python is important for interviews ")
# f1.close()

# f2=open("file2.txt","r")
# print(f2.read())
# # data=f2.readline(10) #to read upto particular character
# # print(data)
# f2.close()

# f2=open("file2.txt","r")
# data=f2.readline() #to read single line 
# print(data)
# f2.close()

# f2=open("file2.txt","r")
# data=f2.readlines() #to read multiple lines
# print(data)
# f2.close()

# f2=open("file2.txt","r")
# data=f2.readlines() 
# print(data)
# data=f2.readline(10)
# print(data)
# f2.close()

# f2=open("file2.txt","r")
# data=f2.readline() 
# print(data)
# print(f2.readable())
# f2.close()


# cursor handle position
# tell()= tell is used to to get the position of a cursor in a file
# seek()= seek() is used to shift/change the position of the cursor in a file
# f3=open("file2.txt","r")
# print(f3.tell())
# print(f3.read(3))
# print(f3.tell())
# print(f3.readline())
# print(f3.tell())
# print(f3.read())
# print(f3.tell())
# print(f3.read())
# print(f3.read(5))

# reverse reading using cursor
# f3=open("file2.txt","r")
# print(f3.tell())
# print(f3.read(3))
# f3.seek(0)
# print(f3.tell())
# print(f3.read(10))
# print(f3.tell())
# f3.seek(15)
# print(f3.tell())


f3=open("file2.txt","rb")
print(f3.tell())
f3.seek(-10,2)
print(f3.tell())
print(f3.read(10))

# print(f3.tell())
# f3.seek(10,1)
# print(f3.tell())
# print(f3.read(10))
# f3.close()

# with open("file2.txt","rb") as f:
#     print(f.read(8))
#     print(f.tell())
#     f.seek(10,1)
#     print(f.tell())
#     print(f.closed)
# print(f.closed)    
   



