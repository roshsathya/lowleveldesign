from datetime import datetime
from .ticket import TicketFactory


class Slot:
    def __init__(self) -> None:
        self.person_obj = None

    def is_occupied(self):
        return bool(self.person_obj)

    def get_time_elapsed(self):
        if not self.is_occupied():
            raise Exception()
        return datetime.utcnow() - self.start_time

    def allot_slot(self, person_obj):
        self.person_obj = person_obj

    def unallot_slot(self):
        self.person_obj = None

    def issue_ticket(self):
        raise Exception()


class NormalSlot(Slot):

    slot_type = "NORMAL"

    def __init__(self) -> None:
        super().__init__()

    def issue_ticket(self, mins):
        Ticket = TicketFactory.get_ticket(NormalSlot.slot_type)
        return Ticket(mins)


class HandicapSlot(Slot):

    slot_type = "SPECIAL"

    def __init__(self) -> None:
        super().__init__()

    def issue_ticket(self, mins):
        Ticket = TicketFactory.get_ticket(NormalSlot.slot_type)
        return Ticket(mins)


class SlotFactory:
    types = {
        "NORMAL": NormalSlot,
        "HANDICAP": HandicapSlot
    }

    @classmethod
    def get_slot(cls, type):
        if type not in cls.types:
            raise Exception()
        return cls.types[type]
