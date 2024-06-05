# The parameters are dynamic not static / the user has to manually enter the parameters
def values(w,y,z):
    start = int(input("Enter the start value: "))
    step = int(input("Enter the step value: "))
    stop = int(input("Enter the stop value: "))

# iterate over the range
for i in range(w,y,z):
    # Print even numbers 
    if i % 2 != 0:
        continue
    print(i)  
values(2,20,2)    

