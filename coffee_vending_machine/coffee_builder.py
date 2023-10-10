
class CoffeeBuilder():

    beans = None
    coffee_types = None
    coffee_temps = None

    def __init__(self) -> None:
        self.current_step = 0
        self.coffee_type_no = None
        self.coffee_temp_no = None
        self.beans_no = None

    @classmethod
    def setup_beans(cls, beans_dict):
        cls.beans = beans_dict

    @classmethod
    def setup_coffee_types(cls, coffee_type_dict):
        cls.coffee_types = coffee_type_dict

    @classmethod
    def setup_coffee_temps(cls, coffee_temp_dict):
        cls.coffee_temps = coffee_temp_dict

    @classmethod
    def get_coffee_beans(cls):
        return [(idx, bean_obj.name) for idx, bean_obj in enumerate(cls.beans)]

    @classmethod
    def get_coffee_types(cls):
        return [(idx, coffee_obj.name) for idx, coffee_obj in enumerate(cls.coffee_types)]

    @classmethod
    def get_coffee_temps(cls):
        return [(idx, coffee_obj.name) for idx, coffee_obj in enumerate(cls.coffee_temps)]

    def set_coffee_type(self, coffee_type_no):
        self.coffee_type_no = coffee_type_no
        self.current_step += 1

    def get_coffee_temp(self):
        coffee_type_obj = CoffeeBuilder.coffee_types[self.coffee_type_no]
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
        for idx, bean_obj in CoffeeBuilder.beans.items():
            if bean_obj.current_quantity > 0:
                output.append((idx, bean_obj.name))
        return output

    def set_coffee_beans(self, beans_no):
        self.beans_no = beans_no
        self.current_step += 1

    def build_coffee(self):
        if self.current_step != 3:
            return
        coffee_type_obj = CoffeeBuilder.coffee_types[self.coffee_type_no]
        beans_obj = CoffeeBuilder.beans[self.beans_no]
        coffee_temp_obj = CoffeeBuilder.coffee_temps[self.coffee_temp_no]

        coffee_type_obj.process_coffee(coffee_temp_obj, beans_obj)
