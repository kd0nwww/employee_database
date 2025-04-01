import sqlite3
from employee import Employee

class EmployeeDAO:
    def __init__(self, database):
        self.__connection = sqlite3.connect(database)
        self.__cursor = self.__connection.cursor()

    def insert(self, employee: Employee):
        sql = '''INSERT INTO employee (name, position, salary, hire_date) VALUES (?, ?, ?, ?)'''
        self.__cursor.execute(sql, (employee.get_name(), employee.get_position(), employee.get_salary(), employee.get_hire_date()))

        self.__connection.commit()
        return self.__cursor.lastrowid
