class Person:

    pass
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    # primeira passada: criar instâncias
    for peo in people:
        result.append(Person(peo["name"], peo["age"]))
    # segunda passada: Ligar cônjuges por referência
    for src, inst in zip(people, result):
        wife_name = src.get("wife")
        husb_name = src.get("husband")
        if wife_name is not None:
            inst.wife = Person.people[wife_name]
        if husb_name is not None:
            inst.husband = Person.people[husb_name]
    return result
