###Create an application that takes in list(use a dict inside a list ) 
# Dictorianaries and perform the following function join,split and replace


list_of_dicts = [{"name":"Samson","age":"20","gender":"male",},
                 {"name":"Rachie","age":"18","gender":"female",},
]
def join(list_of_dicts):
    for i in list_of_dicts:
        print(i)
        print(i["name"])
        print(i["age"])
        print(i["gender"])
        print(i["name"]+i["age"]+i["gender"])

def split(list_of_dicts):
    for i in list_of_dicts:
        print(i)
        print(i["name"])
        print(i["age"])
        print(i["gender"])
        print(i["name"]+i ["age"]+i ["gender"])

def replace(list_of_dicts):
    for i in list_of_dicts:
        print(i)
        print(i["name"])
        print(i["age"])
        print(i["gender"])
        print(i["name"]+i["age"]+i["gender"])

join(list_of_dicts)

split(list_of_dicts)

replace(list_of_dicts)


       

