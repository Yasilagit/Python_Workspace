#C.R.U.D Operation EmployeeBook
class Employee:
    def __init__ (self,empNo,name,age,salary):
        self.empNo=empNo
        self.name=name
        self.age=age
        self.salary = salary
    def printEmployee(self):
        return [self.empNo,self.name,self.age,self.salary]
  
empNo = input("Employee NO: ")
empName = input("Employee Name: ")
age = input("Employee Age: ")
salary = input("Employee Salary: ")
empl =  Employee(empNo,empName,age,salary)
lstEmployee = empl.printEmployee()

for emp in lstEmployee:
    print(emp , end="\t")





