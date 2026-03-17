class Person:

    pass
    people_list = []


    def __init__(self, name: str, age: int) -> None:
            self.name = name
            self.age = age
            Person.people[name] = self


    def create_person_list(people: list) -> list:
        people_list = []
        for index, person in enumerate(people):
            current_person = Person(person["name"], person["age"])
            if "wife" in person:
                current_person.wife = person["wife"]
            else:
                current_person.husband = person["husband"]
            people_list.append(current_person)

        for person in people_list:
            if hasattr(person, "wife"):
                if person.wife != None:
                    person.wife = Person.people[person.wife]
            if hasattr(person, "husband"):
                if person.husband != None:
                    person.husband = Person.people[person.husband]
        return people_list
