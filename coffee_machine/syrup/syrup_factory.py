from .syrup_types import *


class SyrupFactory:
    syrup_types = {
        Vanilla.system_name: Vanilla,
        Strawberry.system_name: Strawberry,
    }

    def __init__(self) -> None:
        pass

    @classmethod
    def get_syrup(cls, syrup_type):
        syrupClass = cls.syrup_types.get(syrup_type)
        if not syrupClass:
            raise Exception
        return syrupClass()
