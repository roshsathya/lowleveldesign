from .bean_types import *


class BeansFactory:
    bean_types = {
        Arabica.system_name: Arabica,
        Robusta.system_name: Robusta,
        Liberica.system_name: Liberica
    }

    def __init__(self) -> None:
        pass

    @classmethod
    def get_bean(cls, bean_type):
        BeanClass = cls.bean_types.get(bean_type)
        if not BeanClass:
            raise Exception
        return BeanClass()
