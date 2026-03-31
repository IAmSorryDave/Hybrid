from hybridz import hybrid
from dataclasses import dataclass


@hybrid
def my_function(*args, c=2, d="baz", z=False, **kwargs):
    return locals().copy()


class MyClass:
    z = True

    def my_bare_method(*args, c=2, d="baz", z=False, **kwargs):
        return my_function(*args, c=c, d=d, z=z, **kwargs)

    my_class_method = classmethod(my_function)

    my_method = my_function

    my_static_method = staticmethod(my_function)

    my_property = property(my_function)


class MySubClass(MyClass):
    d = "qux"


@dataclass
class MyDataClass:
    c: int = 3
    d: str = "baz"
    z: bool = True

    my_method = my_function

    my_property = property(my_function)
