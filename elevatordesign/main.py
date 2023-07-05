RESIDENTIAL = 'RESIDENTIAL'
COMMERCIAL = 'COMMERCIAL'
FREIGHT = 'FREIGHT'


class Elevator:
    def __init__(self, levels, max_capacity) -> None:
        self.levels = levels
        self.current_level = 0
        self.max_capacity = max_capacity
        self.light_bulb_on = False
        self.security_alarm = False
        self.fan_on = False

    def fan_switch(self):
        return not self.fan_on

    def light_bulb_switch(self):
        return not self.light_bulb_on

    def security_alarm_switch(self):
        return not self.security_alarm

    def press_level(self, level):
        if level > self.levels or level < 0:
            raise ValueError(f"Level provided is incorrect")
        if level == self.current_level:
            return
        self.current_level = level

    @classmethod
    def get_best_elevator(cls, *args):
        raise Exception()


class ResidentialElevator(Elevator):
    def __init__(self, levels, max_capacity=10) -> None:
        super().__init__(levels, max_capacity)

    @classmethod
    def get_best_elevator(cls, level):
        pass


class CommercialElevator(Elevator):
    def __init__(self, levels, max_capacity=15) -> None:
        super().__init__(levels, max_capacity)

    @classmethod
    def get_best_elevator(cls, level):
        pass


class FreightElevator(Elevator):
    def __init__(self, levels, max_capacity=30) -> None:
        super().__init__(levels, max_capacity)

    @classmethod
    def get_best_elevator(cls, level):
        pass


class ElevatorFactory:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_elevator_class():
        return {
            RESIDENTIAL: ResidentialElevator,
            COMMERCIAL: CommercialElevator,
            FREIGHT: FreightElevator
        }

    @classmethod
    def get_elevator(cls, levels, elevator_type):
        ElevatorClass = cls.get_elevator_class().get(elevator_type)
        if not ElevatorClass:
            raise ValueError("Incorrect elevator type")
        return ElevatorClass(levels)

    @classmethod
    def get_n_elevators(cls, total_elevators, elevator_type):
        return [cls.get_elevator(elevator_type) for _ in range(total_elevators)]


class ElevatorSystem:
    def __init__(self, levels, elevator_type) -> None:
        self.ElevatorClass = self.get_elevator_class(elevator_type)
        self.elevators = ElevatorFactory.get_n_elevators(levels, elevator_type)

    def get_elevator_class(self, elevator_type):
        ElevatorClass = None
        try:
            ElevatorClass = ElevatorFactory.get_elevator_class(elevator_type)
        except:
            raise Exception("Error in given elevator type")
        return ElevatorClass

    def get_closest_elevator(self, level):
        return self.ElevatorClass.get_best_elevator(level)
