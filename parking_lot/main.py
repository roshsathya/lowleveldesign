from .slot_manager import SlotManager


class ParkingLot:
    def __init__(self) -> None:
        self.slot_manager = SlotManager()

    def setup_slots(self, type, count):
        self.slot_manager.setup_slots(type, count)

    def find_slot(self, person_obj):
        slot_type = person_obj.__class__.slot_type
        is_slot_avalaible = self.slot_manager.is_slot_available(slot_type)
        if not is_slot_avalaible:
            return None
        return self.slot_manager.find_slot(person_obj)
