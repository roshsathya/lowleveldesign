from coffee_machine.water import Water


class Still(Water):
    system_name = "STILL"
    name = "Still"
    price = 0


class Sparkling(Water):
    system_name = "SPARKLING"
    name = "Sparkling"
    price = 2
