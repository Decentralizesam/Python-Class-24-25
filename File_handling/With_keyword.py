# with enables us to explicitly close the file

with open("data.txt", 'w') as file:
    file.write("My name is samson\n")
    file.write("i am a good boy\n")

with open("data.txt", 'r')as file:
    content=file.read()
    print(content)




