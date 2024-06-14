# before forming any operator on a file we first (open)
# W is for write and removes all what in the txt file and xreplace it with the new word 
# a is for append just adds on to the ednd of the existing object or data in the txt file


file=open("data.txt","a")
file.write("My name is samson.\n")
file.close()

