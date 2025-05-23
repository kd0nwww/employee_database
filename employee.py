class Employee:
    def __init__(self, id, name, position, salary, hire_date):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.position
    
    def get_salary(self):
        return self.salary
    
    def get_hire_date(self):
        return self.hire_date
    
    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_position(self, position):
        self.position = position

    def set_salary(self, salary):
        self.salary = salary

    def set_hire_date(self, hire_date):
        self.hire_date = hire_date

    def __str__(self):
        return f"Employee ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Hire Date: {self.hire_date}"