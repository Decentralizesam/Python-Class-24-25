# opening a file we use open(function)
# how to open a file
# Modes "r","w","a","b"

def file_handling():
    file=open("data.txt","r")
    return file.read()
print(file_handling())


file=open("data.txt","r")
lines=file.readlines()
for line in lines:
    print(line,end=" ")
file.close()

file2=open("data.txt","r")
lines2=file2.readlines()
while lines:
    print(lines,end = " ")
    lines=file2.readline()
    file2.close()


# why use read
# Acessing data 
# Data processing
# Data transformations
# Data analysis 


Formats of data 
# Xml format
# csv format
# json format 

webscripting 

file=open("data.txt","r")
lines=file.readlines()
for line in lines:
    print(line,end=" ")
file.close()