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
    
    def get_by_id(self, id):
        sql = '''SELECT * FROM employee WHERE id = ?'''
        self.__cursor.execute(sql, (id,))
        row = self.__cursor.fetchone()
        if row:
            return Employee(row[0], row[1], row[2], row[3], row[4])
        return None
    
    def get_all(self):
        sql = '''SELECT * FROM employee'''
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        employees = []
        for row in rows:
            employees.append(Employee(row[0], row[1], row[2], row[3], row[4]))
        return employees
    
    def update(self, employee: Employee):
        sql = '''UPDATE employee SET name = ?, position = ?, salary = ?, hire_date = ? WHERE id = ?'''
        self.__cursor.execute(sql, (employee.get_name(), employee.get_position(), employee.get_salary(), employee.get_hire_date(), employee.get_id()))
        self.__connection.commit()

        return self.__cursor.rowcount
    
    def delete(self, id):
        sql = '''DELETE FROM employee WHERE id = ?'''
        self.__cursor.execute(sql, (id,))

        self.__connection.commit()

        return self.__cursor.rowcount