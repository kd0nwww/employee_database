# Employee Database

This repository is a Python-based project that demonstrates Object-Oriented Programming (OOP) concepts by implementing an employee database system. The project is structured to manage employee records, including adding, updating, and retrieving employee details.

## Structure

- [employee.py](employee.py) - the file that that is used to create `Employee` instances.
- [database.sqlite](database.sqlite) - the database that contains information about employees.
- [dao.py](dao.py) - the file that deals with database and makes CRUD operations.
- [main.py](main.py) - the file that is used for testing.
- [imgs](imgs) - the directory that contains screenshots of tests.

## Test input/output
### 1. Inserting a new employee
#### Initially the database looks like this:
![screenshot](imgs/b_insert.PNG)

```python
    new_emp = Employee(120321, "Madina Gabbazova", "HR Manager", 45000, "2023-08-23")
    dao.insert(new_emp)
```
![screenshot](imgs/a_insert.PNG)

### Retrieving the employee by ID
```python
    emp = dao.get_by_id(1)
    print(emp)
```
![screenshot](imgs/a_search.PNG)

### Retrieving all employees
```python
    emps = dao.get_all()
    for emp in emps:
        print(emp)
```
![screenshot](imgs/a_search_all.PNG)

### Updating employee
![screenshot](imgs/b_update.PNG)

```python
    emp_update = Employee(1, "Aidin Turdukulov", "Sales Representative", 38000, "2021-01-29")
    dao.update(emp_update)
```

![screenshot](imgs/a_update.PNG)

### Deleting employee
![screenshot](imgs/b_delete.PNG)

```python
    dao.delete(3)
```

![screenshot](imgs/a_delete.PNG)