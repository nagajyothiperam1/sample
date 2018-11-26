class Person:
	pass
	
p1=Person()
p1.fname="jyo"
p1.lname="p"
print(p1)
print(p1.fname+'-'+p1.lname)

class Personn:
	'initializing like a constructor'
	def __init__(self,fname,lname):
	
		self.fname=fname
		self.lname=lname

p1=Personn('jyo','p')
print(p1.fname+' '+p1.lname)
help(Personn)

