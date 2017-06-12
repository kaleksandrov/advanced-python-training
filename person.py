class Person(object):

    employees = {}

    def __init__(self, name, age, salary):
        self.pid = 1
        self.name = name
        self.age = age
        self.salary = salary
        Person.exists(self.pid, self.name)

    def __str__(self):
        return "%s %d %7.2f"% (self.name, self.age, self.salary)

    def __hash__(self):
        return self.pid

    @classmethod
    def exists(cls, pid, name):
        if pid in cls.employees:
            raise Exception("Duplicate person")
        cls.employees[pid] = name


p = Person('bob', 35, 8000)
p = Person('bob', 35, 8000)
print(p)
print(p.__hash__())
