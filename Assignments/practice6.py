# The parameters are dynamic not static / the user has to manually enter the parameters
def values(names):
    start = int(input("Enter the start value: "))
    step = int(input("Enter the step value: "))
    stop = int(input("Enter the stop value: "))

# iterate over the range
for i in range(len(values)):
    # Print even numbers 
    if i % 2 != 0:
        continue
    print(i)  
values(start,step,stop)    

