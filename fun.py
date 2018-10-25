#functions as arguements == higher order functions
def inc(x):
	return x+1
def dec(x):
	return x-1
	
def op(fun,x):
	result=fun(x)
	return result
	
print(op(inc,3))
print(op(dec,3))

#function can return another function.
def a():
	def b():
		print "hello"
	return b 

res=a()
res()
	

