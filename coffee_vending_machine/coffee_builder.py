
class CoffeeBuilder():
    def __init__(self) -> None:
        self.beans = self.setup_beans()
        self.coffee_types = self.setup_coffee_type()

    @classmethod
    def get_coffee_beans(cls):
        return

    def get_coffee_type_no(self, coffee_type_no):
        self.coffee_type_no = coffee_type_no

    def get_coffee_temp_no(self, coffee_temp_no):
        self.coffee_temp_no = coffee_temp_no

    def get_coffee_beans_no(self, beans_no):
        self.beans_no = beans_no

    # {
    #    1: Bean("arabica", "yemen", 1000),
    #    2: Bean("pacas", "yemen", 1000)
    # }
    def setup_beans(self, beans_dict):
        return beans_dict

    # {
    #    1: CoffeeProcessingFactory.get_coffee_object(1),
    #    2: CoffeeProcessingFactory.get_coffee_object(2),
    # }
    def setup_coffee_type(self, coffee_type_dict):
        return coffee_type_dict

    def build_coffee(self, coffee_type_no, coffee_temp_no, beans_no):
        coffee_obj = self.coffee_types[coffee_type_no]
        beans_obj = self.beans[beans_no]
        return coffee_obj.process_coffee(coffee_temp_no, beans_obj)
