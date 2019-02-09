class employee:
    numofemp=0

    sum=0
    def _init_(self,name,family,salary,department):
        self.name=name
        self.family = family
        self.salary = salary
        self.department = department
        employee.numofemp+=1
    def averagesal(self):
        employee.sum+=self.salary


class fulltimeEmp(employee):
    def __init__(self, name, family, salary, department):
        employee._init_(self, name, family, salary, department)
    def averagesal(self):
        super().averagesal()
        self.averagesalary = employee.sum / employee.numofemp
        print(self.averagesalary)


a = fulltimeEmp("Sumanth","Sanakkayla",1000,"cse")
a.averagesal()
b = fulltimeEmp("Nikhil","Sanka",2000,"eee")
b.averagesal()
print("Employee count is "+str(employee.numofemp))