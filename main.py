from employee import Employee
from dao import EmployeeDAO

dao = EmployeeDAO("C:\Coding\Python\OOP\employee_database\database.sqlite")

# Inserting new employee
new_emp = Employee(120321, "Madina Gabbazova", "HR Manager", 45000, "2023-08-23")
dao.insert(new_emp)

# Retrieving employee by ID
emp = dao.get_by_id(1)
print(emp)

# Retrieving all employees
emps = dao.get_all()
for emp in emps:
    print(emp)

# Updating employee
emp_update = Employee(1, "Aidin Turdukulov", "Sales Representative", 38000, "2021-01-29")
dao.update(emp_update)

# Deleting employee
dao.delete(3)