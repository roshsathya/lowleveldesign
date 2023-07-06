class ElevatorTypes:
    RESIDENTIAL = 'RESIDENTIAL'
    COMMERCIAL = 'COMMERCIAL'
    FREIGHT = 'FREIGHT'


class ElevatorStatus:
    UP = 'UP'
    DOWN = 'DOWN'
    HALT = 'HALT'


class LevelButton:
    UP = 'UP'
    DOWN = 'DOWN'


class Elevator:
    def __init__(self, levels, max_capacity) -> None:
        self.levels = levels
        self.current_level = 0
        self.status = ElevatorStatus.HALT
        self.max_capacity = max_capacity
        self.levels_to_halt = []
        self.is_light_bulb_on = False
        self.is_security_alarm_on = False
        self.is_fan_on = False
        self.is_door_status = False

    def fan_switch(self):
        return not self.is_fan_on

    def light_bulb_switch(self):
        return not self.is_light_bulb_on

    def security_alarm_switch(self):
        return not self.is_security_alarm

    def door_switch(self):
        not self.is_door_status
        if not self.levels_to_halt:
            self.status = ElevatorStatus.HALT

    def press_level(self, level, direction):
        if level > self.levels or level < 0:
            raise ValueError(f"Level provided is incorrect")
        if level == self.current_level:
            return
        self.current_level = level

    def select_level(self, level):
        self.levels_to_halt.append(level)

    @classmethod
    def get_best_elevator(cls, *args):
        raise Exception()


class ResidentialElevator(Elevator):
    def __init__(self, levels, max_capacity=10) -> None:
        super().__init__(levels, max_capacity)

    @classmethod
    def get_best_elevator(cls, all_elevators, level, direction):
        closest_elevator = None
        closest_elevator_distance = float("inf")

        for elevator in all_elevators:
            possible_elevator = None

            if elevator.status == ElevatorStatus.HALT:
                possible_elevator = elevator
            elif (elevator.status == ElevatorStatus.DOWN and elevator.current_level > level and direction == LevelButton.DOWN) \
                    or (elevator.status == ElevatorStatus.UP and elevator.current_level < level and direction == LevelButton.UP):
                possible_elevator = elevator

            if possible_elevator and abs(possible_elevator.current_level - level) < closest_elevator_distance:
                closest_elevator = possible_elevator
                closest_elevator_distance = abs(
                    possible_elevator.current_level - level)

        return closest_elevator


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
            ElevatorTypes.RESIDENTIAL: ResidentialElevator,
            ElevatorTypes.COMMERCIAL: CommercialElevator,
            ElevatorTypes.FREIGHT: FreightElevator
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
    def __init__(self, total_elevators, levels, elevator_type) -> None:
        self.ElevatorClass = self.get_elevator_class(elevator_type)
        self.elevators = ElevatorFactory.get_n_elevators(
            total_elevators, levels, elevator_type)

    def get_elevator_class(self, elevator_type):
        ElevatorClass = None
        try:
            ElevatorClass = ElevatorFactory.get_elevator_class(elevator_type)
        except:
            raise Exception("Error in given elevator type")
        return ElevatorClass

    def press_level_button(self, level, direction):
        elevator = self.ElevatorClass.get_best_elevator(
            self.elevators, level, direction)
        if elevator.status == ElevatorStatus.HALT:
            if elevator.current_level > level:
                elevator.status = ElevatorStatus.DOWN
            elif elevator.current_level < level:
                elevator.status = ElevatorStatus.UP
        elevator.current_level = level
