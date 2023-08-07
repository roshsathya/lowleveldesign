import signal


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


# This class has the capability of counting the total number of people
# within the elevator and also signaling if the sensor is on/off
# (which means an individual is keeping the elevator at halt)

class ElevatorDoorSensor:
    def __init__(self) -> None:
        self.sensor = False
        self.current_capacity = 0
        self.setup_signal()

    def setup_signal(self):
        signal.signal(signal.SIGUSR1, self.capacity_signal_handler)
        signal.siginterrupt(signal.SIGUSR1, False)

    def toggle_sensor(self, current_capacity):
        self.current_capacity = current_capacity
        return not self.sensor

    def get_sensor_status(self):
        return self.sensor

    def get_capacity(self):
        return self.current_capacity

    def capacity_signal_handler(self, signal):
        self.current_capacity = signal


class Elevator:
    def __init__(self, levels, max_capacity) -> None:
        self.levels = [not bool(level) for level in range(levels)]
        self.current_level = 0
        self.status = ElevatorStatus.HALT
        self.max_capacity = max_capacity
        self.is_light_bulb_on = False
        self.is_security_alarm_on = False
        self.is_fan_on = False
        self.is_door_status = False
        self.sensor = ElevatorDoorSensor()

    def fan_switch(self):
        return not self.is_fan_on

    def light_bulb_switch(self):
        return not self.is_light_bulb_on

    def security_alarm_switch(self):
        return not self.is_security_alarm

    def door_switch(self):
        if not self.is_door_status:
            return True
        current_weight = self.sensor.get_capacity()
        if current_weight >= self.max_capacity:
            return True
        return False

    def press_level(self, level, direction):
        if level > len(self.levels) or level < 0:
            raise ValueError(f"Level provided is incorrect")
        if level == self.current_level:
            return
        self.levels[level] = True
        self.move(direction)

    def move(self, direction):
        if direction == LevelButton.UP:
            condition = self.current_level < len(
                self.levels)
            self.status = ElevatorStatus.UP
        else:
            condition = self.current_level >= 0
            self.status = ElevatorStatus.DOWN

        while condition:
            if self.levels[self.current_level]:
                self.status = ElevatorStatus.HALT
                break
            if direction == LevelButton.UP:
                self.current_level += 1
            else:
                self.current_level -= 1

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
    elevator_types = {
        ElevatorTypes.RESIDENTIAL: ResidentialElevator,
        ElevatorTypes.COMMERCIAL: CommercialElevator,
        ElevatorTypes.FREIGHT: FreightElevator
    }

    def __init__(self) -> None:
        pass

    @classmethod
    def get_elevator_class(cls, elevator):
        return cls.elevator_types.get(elevator)

    @classmethod
    def get_elevator(cls, levels, elevator_type):
        ElevatorClass = cls.get_elevator_class(elevator_type)
        if not ElevatorClass:
            raise ValueError("Incorrect elevator type")
        return ElevatorClass(levels)

    @classmethod
    def get_n_elevators(cls, total_elevators, elevator_type):
        return [cls.get_elevator(elevator_type) for _ in range(total_elevators)]


class ElevatorSystem:
    def __init__(self, levels: int, elevator_types: dict) -> None:
        self.elevators_dict = self.set_elevator_dict(levels, elevator_types)

    def set_elevator_dict(self, levels, elevator_types):
        elevators_dict = {}
        for elevator_type, count in elevator_types.items():
            elevators_dict[elevator_type] = [ElevatorFactory.get_elevator(
                levels, elevator_type) for _ in range(count)]
        return elevators_dict

    def press_level_button(self, level, direction, elevator_type):
        ElevatorClass = ElevatorFactory.elevator_types(elevator_type)
        elevator = ElevatorClass.get_best_elevator(
            self.elevators_dict[elevator_type], level, direction)
        elevator.levels[level] = True
        elevator_direction = LevelButton.UP if level > elevator.current_level else LevelButton.DOWN
        elevator.move(elevator_direction)


# Problems to address
# - Having different kind of elevators - dict
# - Keeping state of different elevators
# - Adding buttons within elevator
# - Person class
# - Checking capacity of the elevator
