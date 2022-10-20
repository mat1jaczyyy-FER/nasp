class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increase_age(self):
        self.age += 1

class PersonDetail(Person):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

first_person = Person('Marko', 39)
second_person = Person('Ivan', 17)
second_person.increase_age()

first_person_detail = PersonDetail('Ana', 25, 'Unska 3')
first_person_detail.increase_age()
