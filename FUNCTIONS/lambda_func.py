add = lambda x,y :x+y
print(add(10,20))

nums=list(range(20))
square = list(map(lambda x:x**2,nums))
## map is an iterators(for loop and maps are iterators)
print(square)

list(range(1,20,2))

def myfunc (n):
	return lambda a : a * n
mydoubler = myfunc(5)
print(mydoubler(11))