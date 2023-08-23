from datetime import datetime, timedelta


class Ticket:
    def __init__(self, base_value) -> None:
        self.base_value = base_value
        self.start_time = datetime.utcnow()
        self.end_time = None

    def get_cost(self, discount):
        return self.base_value - discount

    def check_ticket(self):
        current_time = datetime.utcnow()
        base_fare = self.base_value * (self.end_time - self.start_time).mins
        if current_time < self.end_time:
            return base_fare
        return base_fare + 10


class NormalTicket(Ticket):
    def __init__(self, total_mins) -> None:
        super().__init__(20)
        self.end_time = self.start_time + timedelta(minutes=total_mins)


class FirstRespondersTicket(Ticket):
    def __init__(self, total_mins) -> None:
        super().__init__(5)
        self.end_time = self.start_time + timedelta(minutes=total_mins)


class TicketFactory:

    types = {
        'NORMAL': NormalTicket,
        'SPECIAL': FirstRespondersTicket
    }

    @classmethod
    def get_ticket(cls, type):
        if type not in cls.types:
            raise Exception()
        return cls.types[type]
