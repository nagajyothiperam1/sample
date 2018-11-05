class Add2:
	def addition(self):
		a,b=1,2
		return a+b
		
class Add3(Add2): 
	def addition(self):
		a,b,c=1,2,3
		return a+b+c

a1=Add2()
a2=Add3()
print(a1.addition())
print(a2.addition())
		