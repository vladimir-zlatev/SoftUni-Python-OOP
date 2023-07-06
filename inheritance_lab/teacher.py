from inheritance_lab.person import Person
from inheritance_lab.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."