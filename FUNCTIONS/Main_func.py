def main(name):
    print(f"hello,{name}")

def main2():
    first_name=input("First Name :")
    main(first_name)

if __name__ == "__main__":## checks if the script is being run in the main programm
    main2()




x = lambda num1,num2: num1+num2
