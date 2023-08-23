class Person:
    def __init__(self) -> None:
        pass


class Student(Person):
    slot_type = "NORMAL"

    def __init__(self) -> None:
        super().__init__()


class Nurse(Person):
    slot_type = "NORMAL"

    def __init__(self) -> None:
        super().__init__()


class PersonFactory:
    types = {
        'NURSE': Nurse,
        'STUDENT': Student
    }

    @classmethod
    def get_person(cls, type):
        if type not in cls.types:
            raise Exception()
        return cls.types[type]
