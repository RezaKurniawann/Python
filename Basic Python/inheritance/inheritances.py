class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    def calculate_bonus(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def work(self):
        return f"{self.name} is managing the {self.department} department."

    def get_details(self):
        return super().get_details() + f", Department: {self.department}"

    def calculate_bonus(self):
        return self.salary * 0.1

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        return f"{self.name} is writing code in {self.programming_language}."

    def get_details(self):
        return super().get_details() + f", Programming Language: {self.programming_language}"

    def calculate_bonus(self):
        return self.salary * 0.05

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise ValueError("Only Employee objects can be added")

    def get_all_details(self):
        details = [employee.get_details() for employee in self.employees]
        return "\n".join(details)

    def calculate_total_bonus(self):
        total_bonus = sum(employee.calculate_bonus() for employee in self.employees)
        return total_bonus

# Example usage
manager = Manager("Alice", 90000, "IT")
developer = Developer("Bob", 80000, "Python")

company = Company()
company.add_employee(manager)
company.add_employee(developer)

print(company.get_all_details())
print(manager.work())
print(developer.work())
print(f"Total Bonus: {company.calculate_total_bonus()}")
