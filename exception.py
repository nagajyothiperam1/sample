try:
	a=0
	b=1
	if a==0:
		raise TypeError('operand must not be 0')
	
	c=a+b
	print(c)
except TypeError as e:
	print(e)
	

class CustomError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return str(self.value)
def sample(a,b):
	try:
		if a==0:
			raise CustomError('operand must not be 0')
	
		c=a+b
		print(c)
	except CustomError as e:
		print(e)	
	else:
		print("When no exception occurs")
	finally:
		print("excecutes irresptive of above code")
print("first")
print(sample(1,1))
print("second")
print(sample(0,1))
