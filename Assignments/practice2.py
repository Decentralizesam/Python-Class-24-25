#: REMOVE

numbers = [2,4,7,9]
# remove 4 from the list
numbers.remove(4)
print(numbers) 
# Output: [2, 7, 9]

names = ["sam","mary","sarah","john"]
# remove "mary" from the list
names.remove("mary")
print(names)
# Output: ['sam', 'sarah', 'john']


# : POP

numbers = [2,4,7,9]
# remove the last item from the list
numbers.pop()
print(numbers)
# Output: [2, 4, 7]

names = ["DC","95","10","Deng"]
# remove the last item from the list
names.pop()
print(names)
# Output: ['DC', '95', '10']

# : EXTEND

numbers = [2,4,7,9]
numbers.extend([12,14,16])
print(numbers)
#Output: [2,4,7,9,12,14,16]

names = ["DC","95","10","Deng"]
names.extend(["sam","mary","sarah","john"])
print(names)
# Output: ['DC', '95', '10', 'Deng','sam','mary','sarah','john']

# : CONCATENATION

numbers = [2,4,7,9]
numbers += [12,14,16]
print(numbers)
# Output: [2,4,7,9,12,14,16]

names = ["DC","95","10","Deng"]
names += ["sam","mary","sarah","john"]
print(names)
# Output: ['DC', '95', '10', 'Deng','sam','mary','sarah','john']

# : COUNT

numbers = [2,4,7,9]
print(numbers.count(4))

names = ["DC","95","10","Deng"]
print(names.count("DC"))

# : SORT

numbers = [2,4,7,9]
numbers.sort()
print(numbers)

names = ["DC","95","10","Deng"]
names.sort()
print(names)

# : REVERSE

numbers = [2,4,7,9]
numbers.reverse()
print(numbers)

names = ["DC","95","10","Deng"]
names.reverse()
print(names)



