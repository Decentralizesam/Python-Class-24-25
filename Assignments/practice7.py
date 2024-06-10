###Create an application that takes in list(use a dict inside a list ) 
# Dictorianaries and perform the following function join,split and replace


list_of_dicts = [{"name":"Samson","age":"a","gender":"male",}]

sentence= " " .join(list_of_dicts)
print(sentence)


sentence = list_of_dicts.split(",")
print(sentence)

sentence = list_of_dicts.replace("Samson","sam")
print(sentence)




