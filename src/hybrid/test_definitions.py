from hybrid import hybrid
from dataclasses import dataclass, field
from typing import List, Dict

@hybrid
def my_function(*args, c=2, d='baz', z=False , **kwargs):
    return locals().copy()       

class MyClass:

    z = True

    def my_bare_method(*args, c=2, d='baz', z=False , **kwargs):
        return my_function(*args, c=c, d=d, z=z, **kwargs)

    my_class_method = classmethod(my_function)

    my_method = my_function

    my_static_method = staticmethod(my_function)

class MySubClass(MyClass):

    d = 'qux'

@dataclass
class MyDataClass:
    c: int = 2
    d: str = 'baz'
    z: bool = False


# ===== Different field counts =====

@dataclass
class DataclassSingleField:
    """Dataclass with just one field"""
    value: int = 42


@dataclass
class DataclassMultipleFields:
    """Dataclass with many fields"""
    a: int = 1
    b: str = 'alpha'
    c: float = 3.14
    d: bool = True
    e: list = field(default_factory=list)


# ===== Required vs Optional Fields =====

@dataclass
class DataclassRequiredFields:
    """Dataclass with required fields (no defaults)"""
    name: str
    age: int
    email: str


@dataclass
class DataclassMixedFields:
    """Dataclass with mix of required and optional fields"""
    required_field: str
    optional_field: int = 10
    another_required: bool = False


# ===== Different Types =====

@dataclass
class DataclassDifferentTypes:
    """Dataclass with various Python types"""
    int_field: int = 42
    str_field: str = 'hello'
    float_field: float = 3.14
    bool_field: bool = True
    list_field: List[int] = field(default_factory=lambda: [1, 2, 3])
    dict_field: Dict[str, int] = field(default_factory=lambda: {'key': 1})


# ===== With __post_init__ =====

@dataclass
class DataclassWithPostInit:
    """Dataclass that computes fields in __post_init__"""
    x: int = 5
    y: int = 10
    computed_sum: int = field(init=False)
    
    def __post_init__(self):
        self.computed_sum = self.x + self.y


# ===== Inheritance =====

@dataclass
class DataclassParent:
    """Parent dataclass"""
    parent_field: str = 'parent'
    shared_field: int = 100


@dataclass
class DataclassChild(DataclassParent):
    """Child dataclass inheriting from parent"""
    child_field: str = 'child'


# ===== With __slots__ =====

@dataclass(slots=True)
class DataclassWithSlots:
    """Dataclass using __slots__ for memory efficiency"""
    slot_field_a: int = 1
    slot_field_b: str = 'slot'
    slot_field_c: bool = False


@dataclass(slots=True)
class DataclassWithSlotsAndPostInit:
    """Dataclass with both __slots__ and __post_init__"""
    x: int = 3
    y: int = 4
    magnitude: float = field(init=False)
    
    def __post_init__(self):
        self.magnitude = (self.x ** 2 + self.y ** 2) ** 0.5


# ===== Complex Inheritance with Slots =====

@dataclass(slots=True)
class DataclassSlotsParent:
    """Parent dataclass with slots"""
    parent_slot_field: str = 'parent_slot'


@dataclass(slots=True)
class DataclassSlotsChild(DataclassSlotsParent):
    """Child dataclass inheriting from slotted parent"""
    child_slot_field: int = 99
    