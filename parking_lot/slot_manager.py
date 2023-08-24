from .slot import SlotFactory


class SlotManager:
    def __init__(self) -> None:
        self.slots = {}

    def setup_slots(self, type, total):
        if type in self.slots:
            raise Exception()
        slots = [SlotFactory.get_slot(type) for _ in range(total)]
        self.slots[type] = {
            "slots": slots,
            "total_available": total
        }

    def is_slot_available(self, type):
        if type not in self.slots:
            return False
        return bool(self.slots[type])

    def find_slot(self, type, person_obj):
        slots_availabe = self.is_slot_available(type)
        if not slots_availabe:
            return None
        for Slot in self.slots:
            if Slot.is_occupied():
                continue
            Slot.allot_slot(person_obj)
