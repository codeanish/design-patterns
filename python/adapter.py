from datetime import datetime

# Person from our system  
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

# Person from another system with a slightly different schema 
# And not the same functions available
class PersonFromAnotherSystem:
    def __init__(self, name: str, year_of_birth: int):
        self.name = name
        self.year_of_birth = year_of_birth

# Use an adapter to wrap the personfromanotherschema and provide
# the function which we want to use in another place
class PersonAdapter:
    def __init__(self, person: PersonFromAnotherSystem):
        self.person = person

    def get_age(self):
        return datetime.now().year - self.person.year_of_birth

# Function which takes a person object - not using type hints here
# as this could be of any actual type, so long as it has a get_age
# function on it
def print_age(person):
    print(person.get_age())


if __name__ == "__main__":
    person = Person("Anish", 39)
    person_from_elsewhere = PersonFromAnotherSystem("Raksha", 1985)
    adapted_person = PersonAdapter(person_from_elsewhere)
    print_age(person)
    print_age(adapted_person)
