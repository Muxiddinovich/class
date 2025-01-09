class Person:
    def __init__(self, first_name, last_name, year):
        self.first_name=first_name
        self.last_name=last_name
        self.year=year

person1=Person("Sherbek", "Kubayev", 2008)

a=5

print(type(Person))




class Person:
    def __init__(self, first_name, last_name, year):
        self.first_name=first_name
        self.last_name=last_name
        self.year=year

    def get_info(self):



         
        print(f"Mening ismim {self.first_name}!")





    def get_age(self):
        return 2025-self.year









person1=Person("Sherbek", "Kubayev", 2008)
person1.get_info()

print(person1.get_age())