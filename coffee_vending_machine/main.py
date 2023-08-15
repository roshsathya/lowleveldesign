"""
- A machine which makes any mainstream coffee by a click of a button
- Money can be paid in cash or by card

Use Cases
1. The following are the use cases for handling coffee
- Machine should handle various kinds of coffee
- The types of beans
- Should be able to select the kind of roast
- Temperature - Hot or cold

2. Payment
- Means - Cash or Card
- if cash, money must be deposited within the machine, to provide change in return if any

3. Security
- Need a mechanism for authenticated users to open the machine
- Something similar to how a safe is secured, which is a pin but also include a key or an otp
- For this designs sake, we shall assume its a key
"""

from .coffee_builder import CoffeeBuilder


class UserInterface:
    def __init__(self) -> None:
        self.initial_setup()

    def initial_setup(self):
        beans_dict = {}
        # {
        #    1: BeanFactory.get_coffee_object(1),
        #    2: BeanFactory.get_coffee_object(2),
        # }
        CoffeeBuilder.setup_beans(beans_dict)
        coffee_type_dict = {}
        # {
        #    1: CoffeeProcessingFactory.get_coffee_object(1),
        #    2: CoffeeProcessingFactory.get_coffee_object(2),
        # }
        CoffeeBuilder.setup_coffee_types(coffee_type_dict)
        coffee_temp_dict = {}
        # {
        #    1: CoffeeTempFactory.get_coffee_object(1),
        #    2: CoffeeTempFactory.get_coffee_object(2),
        # }
        CoffeeBuilder.setup_coffee_types(coffee_temp_dict)

    def start_process(self):
        coffee_builder = CoffeeBuilder()

    def process_payment(self):
        pass
