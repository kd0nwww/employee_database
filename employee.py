class Employee:
    def __init__(self, id, name, position, salary, hire_date):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date

    def __str__(self):
        return f"Employee ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Hire Date: {self.hire_date}"
    
emp = Employee(1, "John Doe", "Software Engineer", 70000, "2023-01-01")
print(emp)