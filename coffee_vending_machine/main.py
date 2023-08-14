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
        self.current_step = 0
        self.coffee_type_no = None
        self.coffee_temp_no = None
        self.beans_no = None
        self.coffee_builder = CoffeeBuilder()

    def get_coffee_type(self):
        return [(idx, coffee_obj.name) for idx, coffee_obj in enumerate(self.coffee_builder.coffee_types)]

    def set_coffee_type(self, coffee_type_no):
        self.coffee_type_no = coffee_type_no
        self.current_step += 1

    def get_coffee_temp(self):
        coffee_type_obj = self.coffee_builder.coffee_types[self.coffee_type_no]
        output = []
        for coffee_temp, coffee_temp_info in coffee_type_obj.coffee_temp.items():
            if coffee_temp_info['can_be_served']:
                output.append((coffee_temp_info['key'], coffee_temp))
        return output

    def set_coffee_temperature(self, coffee_temp_no):
        self.coffee_temp_no = coffee_temp_no
        self.current_step += 1

    def get_coffee_beans(self):
        output = []
        for idx, bean_obj in self.coffee_builder.beans.items():
            if bean_obj.current_quantity > 0:
                output.append((idx, bean_obj.name))
        return output

    def set_coffee_beans(self, beans_no):
        self.beans_no = beans_no
        self.current_step += 1

    def start_process(self):
        self.build_coffee()

    def build_coffee(self):
        if self.current_step != 3:
            return
        return self.coffee_builder.build_coffee(
            self.coffee_type_no, self.coffee_temp_no, self.beans_no)

    def process_payment(self):
        pass
