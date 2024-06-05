

def grade(mark):
    match mark:
        case mark if marks >=80:
            print("A")
        case mark if marks >=75:
            print('B')
        case mark if marks >=70:
            print('c')
        case mark if marks >=60:
            print('D')
        case _:

                print('F')
m =int(input("enter a grade"))
grade(m)











