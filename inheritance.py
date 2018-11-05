class Personn:
	'initializing like a constructor'
	def __init__(self,fname,lname):
	
		self.fname=fname
		self.lname=lname

class Employee(Personn):
	def __init__(self,fname,lname,empid):
		Personn.__init__(self,fname,lname)
		self.empid=empid

p1=Personn('jyothi','peram')
print(p1.fname+' '+p1.lname)
e1=Employee('jyo','p','123')
print(e1.fname+' '+e1.lname+' '+e1.empid)

class Employeeslist(list):
	def search(self,name):
		matched_employees=[]
		for employee in self:
			if name in employee.fname:
				matched_employees.append(employee.fname)
		return matched_employees
		
class Emp(Personn):
	all_emp=Employeeslist()	
	def __init__(self,fname,lname,empid):
		Personn.__init__(self,fname,lname)
		self.empid=empid
		Emp.all_emp.append(self)
		

e1=Emp('jyo','p',123)
e2=Emp('abc','cd',234)
print(Emp.all_emp.search('j'))
print(Emp.all_emp)

		