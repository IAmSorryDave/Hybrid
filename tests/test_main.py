
import pytest

from hybrid import (
    my_function, MyClass, MySubClass, MyDataClass,
    DataclassSingleField, DataclassMultipleFields,
    DataclassRequiredFields, DataclassMixedFields,
    DataclassDifferentTypes, DataclassWithPostInit,
    DataclassParent, DataclassChild,
    DataclassWithSlots, DataclassWithSlotsAndPostInit,
    DataclassSlotsParent, DataclassSlotsChild
)

def test_my_function():

    function_namespace = my_function()

    function_variables = function_namespace.keys()
    
    assert 'c' in function_variables
    assert 'd' in function_variables
    assert 'z' in function_variables
    assert function_namespace['c'] == 2
    assert function_namespace['d'] == 'baz'
    assert function_namespace['z'] == False

def test_my_bare_method():

    bare_method_namespace = MyClass.my_bare_method()

    bare_method_variables = bare_method_namespace.keys()
    
    assert 'c' in bare_method_variables
    assert 'd' in bare_method_variables
    assert 'z' in bare_method_variables
    assert bare_method_namespace['c'] == 2
    assert bare_method_namespace['d'] == 'baz'
    assert bare_method_namespace['z'] == False


def test_my_method():

    my_instance = MyClass()

    method_namespace = my_instance.my_method()

    method_variables = method_namespace.keys()
    
    assert 'c' in method_variables
    assert 'd' in method_variables
    assert 'z' in method_variables
    assert method_namespace['c'] == 2
    assert method_namespace['d'] == 'baz'
    assert method_namespace['z'] == True

def test_my_class_method():

    class_method_namespace = MyClass.my_class_method()

    class_method_variables = class_method_namespace.keys()
    
    assert 'c' in class_method_namespace
    assert 'd' in class_method_namespace
    assert 'z' in class_method_namespace
    assert class_method_namespace['c'] == 2
    assert class_method_namespace['d'] == 'baz'
    assert class_method_namespace['z'] == True

def test_my_static_method():

    static_method_namespace = MyClass.my_static_method()

    static_method_variables = static_method_namespace.keys()

    assert 'c' in static_method_namespace
    assert 'd' in static_method_namespace
    assert 'z' in static_method_namespace
    assert static_method_namespace['c'] == 2
    assert static_method_namespace['d'] == 'baz'
    assert static_method_namespace['z'] == False

def test_my_method_in_subclass():

    my_instance = MySubClass()

    method_namespace = my_instance.my_method()

    method_variables = method_namespace.keys()
    
    assert 'c' in method_variables
    assert 'd' in method_variables
    assert 'z' in method_variables
    assert method_namespace['c'] == 2
    assert method_namespace['d'] == 'qux'
    assert method_namespace['z'] == True

def test_my_classmethod_in_subclass():

    class_method_namespace = MySubClass.my_class_method()

    class_method_variables = class_method_namespace.keys()
    
    assert 'c' in class_method_namespace
    assert 'd' in class_method_namespace
    assert 'z' in class_method_namespace
    assert class_method_namespace['c'] == 2
    assert class_method_namespace['d'] == 'qux'
    assert class_method_namespace['z'] == True

def test_my_static_method_in_subclass():

    static_method_namespace = MySubClass.my_static_method()

    static_method_variables = static_method_namespace.keys()

    assert 'c' in static_method_namespace
    assert 'd' in static_method_namespace
    assert 'z' in static_method_namespace
    assert static_method_namespace['c'] == 2
    assert static_method_namespace['d'] == 'baz'
    assert static_method_namespace['z'] == False

def test_my_bare_method_in_subclass():

    bare_method_namespace = MySubClass.my_bare_method()

    bare_method_variables = bare_method_namespace.keys()
    
    assert 'c' in bare_method_variables
    assert 'd' in bare_method_variables
    assert 'z' in bare_method_variables
    assert bare_method_namespace['c'] == 2
    assert bare_method_namespace['d'] == 'baz'
    assert bare_method_namespace['z'] == False


def test_my_dataclass():

    dataclass_instance = MyDataClass()

    dataclass_namespace = dataclass_instance.__dict__

    dataclass_variables = dataclass_namespace.keys()

    assert 'c' in dataclass_variables
    assert 'd' in dataclass_variables
    assert 'z' in dataclass_variables
    assert dataclass_namespace['c'] == 2
    assert dataclass_namespace['d'] == 'baz'
    assert dataclass_namespace['z'] == False


# Tests with single positional argument
def test_my_function_with_positional_arg():
    function_namespace = my_function('arg1')
    
    assert 'args' in function_namespace
    assert function_namespace['args'] == ('arg1',)
    assert function_namespace['c'] == 2
    assert function_namespace['d'] == 'baz'
    assert function_namespace['z'] == False

def test_my_function_with_multiple_positional_args():
    function_namespace = my_function('arg1', 'arg2', 'arg3')
    
    assert 'args' in function_namespace
    assert function_namespace['args'] == ('arg1', 'arg2', 'arg3')
    assert function_namespace['c'] == 2
    assert function_namespace['d'] == 'baz'
    assert function_namespace['z'] == False


# Tests for methods with positional arguments
def test_my_method_with_positional_arg():
    my_instance = MyClass()
    method_namespace = my_instance.my_method('arg1')
    
    assert 'args' in method_namespace
    assert method_namespace['args'] == ('arg1',)
    assert method_namespace['c'] == 2
    assert method_namespace['d'] == 'baz'
    assert method_namespace['z'] == True

def test_my_method_with_multiple_positional_args():
    my_instance = MyClass()
    method_namespace = my_instance.my_method('arg1', 'arg2')
    
    assert 'args' in method_namespace
    assert method_namespace['args'] == ('arg1', 'arg2')
    assert method_namespace['c'] == 2
    assert method_namespace['d'] == 'baz'
    assert method_namespace['z'] == True

# Tests for class methods with positional arguments
def test_my_class_method_with_positional_arg():
    class_method_namespace = MyClass.my_class_method('arg1')
    
    assert 'args' in class_method_namespace
    assert class_method_namespace['args'] == ('arg1',)
    assert class_method_namespace['c'] == 2
    assert class_method_namespace['d'] == 'baz'
    assert class_method_namespace['z'] == True

def test_my_class_method_with_multiple_positional_args():
    class_method_namespace = MyClass.my_class_method('arg1', 'arg2', 'arg3')
    
    assert 'args' in class_method_namespace
    assert class_method_namespace['args'] == ('arg1', 'arg2', 'arg3')
    assert class_method_namespace['c'] == 2
    assert class_method_namespace['d'] == 'baz'
    assert class_method_namespace['z'] == True

# Tests for static methods with positional arguments
def test_my_static_method_with_positional_arg():
    static_method_namespace = MyClass.my_static_method('arg1')
    
    assert 'args' in static_method_namespace
    assert static_method_namespace['args'] == ('arg1',)
    assert static_method_namespace['c'] == 2
    assert static_method_namespace['d'] == 'baz'
    assert static_method_namespace['z'] == False

def test_my_static_method_with_multiple_positional_args():
    static_method_namespace = MyClass.my_static_method('arg1', 'arg2')
    
    assert 'args' in static_method_namespace
    assert static_method_namespace['args'] == ('arg1', 'arg2')
    assert static_method_namespace['c'] == 2
    assert static_method_namespace['d'] == 'baz'
    assert static_method_namespace['z'] == False

# Tests for bare methods with positional arguments
def test_my_bare_method_with_positional_arg():
    bare_method_namespace = MyClass.my_bare_method('arg1')
    
    assert 'args' in bare_method_namespace
    assert bare_method_namespace['args'] == ('arg1',)
    assert bare_method_namespace['c'] == 2
    assert bare_method_namespace['d'] == 'baz'
    assert bare_method_namespace['z'] == False


# Tests for subclass methods with positional arguments
def test_my_method_in_subclass_with_positional_arg():
    my_instance = MySubClass()
    method_namespace = my_instance.my_method('arg1', 'arg2')
    
    assert 'args' in method_namespace
    assert method_namespace['args'] == ('arg1', 'arg2')
    assert method_namespace['c'] == 2
    assert method_namespace['d'] == 'qux'  # From subclass
    assert method_namespace['z'] == True

def test_my_classmethod_in_subclass_with_positional_arg():
    class_method_namespace = MySubClass.my_class_method('arg1')
    
    assert 'args' in class_method_namespace
    assert class_method_namespace['args'] == ('arg1',)
    assert class_method_namespace['c'] == 2
    assert class_method_namespace['d'] == 'qux'  # From subclass

def test_my_static_method_in_subclass_with_positional_arg():
    static_method_namespace = MySubClass.my_static_method('arg1')
    
    assert 'args' in static_method_namespace
    assert static_method_namespace['args'] == ('arg1',)
    assert static_method_namespace['c'] == 2
    assert static_method_namespace['d'] == 'baz'  # From parent class

# Tests with mixed positional and keyword arguments
def test_my_function_with_positional_and_keyword_args():
    function_namespace = my_function('arg1', 'arg2', c=5, d='custom')
    
    assert 'args' in function_namespace
    assert function_namespace['args'] == ('arg1', 'arg2')
    assert function_namespace['c'] == 5
    assert function_namespace['d'] == 'custom'
    assert function_namespace['z'] == False

def test_my_method_with_positional_and_keyword_args():
    my_instance = MyClass()
    method_namespace = my_instance.my_method('arg1', z=False)
    
    assert 'args' in method_namespace
    assert method_namespace['args'] == ('arg1',)
    assert method_namespace['c'] == 2
    assert method_namespace['d'] == 'baz'
    assert method_namespace['z'] == False  # Override from class


# ===== Single Field Tests =====

def test_dataclass_single_field():
    instance = DataclassSingleField()
    namespace = instance.__dict__
    
    assert 'value' in namespace
    assert namespace['value'] == 42


def test_dataclass_single_field_custom_value():
    instance = DataclassSingleField(value=100)
    namespace = instance.__dict__
    
    assert namespace['value'] == 100


# ===== Multiple Fields Tests =====

def test_dataclass_multiple_fields():
    instance = DataclassMultipleFields()
    namespace = instance.__dict__
    
    assert namespace['a'] == 1
    assert namespace['b'] == 'alpha'
    assert namespace['c'] == 3.14
    assert namespace['d'] == True
    assert namespace['e'] == []


# ===== Required vs Optional Fields Tests =====

def test_dataclass_required_fields():
    instance = DataclassRequiredFields(name='John', age=30, email='john@example.com')
    namespace = instance.__dict__
    
    assert namespace['name'] == 'John'
    assert namespace['age'] == 30
    assert namespace['email'] == 'john@example.com'


def test_dataclass_mixed_fields_with_required():
    instance = DataclassMixedFields(required_field='test', another_required=True)
    namespace = instance.__dict__
    
    assert namespace['required_field'] == 'test'
    assert namespace['optional_field'] == 10
    assert namespace['another_required'] == True


def test_dataclass_mixed_fields_override_optional():
    instance = DataclassMixedFields(required_field='test', optional_field=20, another_required=False)
    namespace = instance.__dict__
    
    assert namespace['optional_field'] == 20
    assert namespace['another_required'] == False


# ===== Different Types Tests =====

def test_dataclass_different_types():
    instance = DataclassDifferentTypes()
    namespace = instance.__dict__
    
    assert isinstance(namespace['int_field'], int)
    assert isinstance(namespace['str_field'], str)
    assert isinstance(namespace['float_field'], float)
    assert isinstance(namespace['bool_field'], bool)
    assert isinstance(namespace['list_field'], list)
    assert isinstance(namespace['dict_field'], dict)


def test_dataclass_different_types_custom_values():
    instance = DataclassDifferentTypes(
        int_field=100,
        str_field='world',
        float_field=2.71,
        bool_field=False,
        list_field=[5, 6, 7],
        dict_field={'new_key': 2}
    )
    namespace = instance.__dict__
    
    assert namespace['int_field'] == 100
    assert namespace['str_field'] == 'world'
    assert namespace['float_field'] == 2.71
    assert namespace['bool_field'] == False
    assert namespace['list_field'] == [5, 6, 7]
    assert namespace['dict_field'] == {'new_key': 2}


# ===== __post_init__ Tests =====

def test_dataclass_with_post_init():
    instance = DataclassWithPostInit()
    namespace = instance.__dict__
    
    assert namespace['x'] == 5
    assert namespace['y'] == 10
    assert namespace['computed_sum'] == 15


def test_dataclass_with_post_init_custom_values():
    instance = DataclassWithPostInit(x=20, y=30)
    namespace = instance.__dict__
    
    assert namespace['computed_sum'] == 50


# ===== Inheritance Tests =====

def test_dataclass_inheritance():
    instance = DataclassChild()
    namespace = instance.__dict__
    
    assert namespace['parent_field'] == 'parent'
    assert namespace['shared_field'] == 100
    assert namespace['child_field'] == 'child'


def test_dataclass_inheritance_override():
    instance = DataclassChild(parent_field='new_parent', shared_field=200, child_field='new_child')
    namespace = instance.__dict__
    
    assert namespace['parent_field'] == 'new_parent'
    assert namespace['shared_field'] == 200
    assert namespace['child_field'] == 'new_child'


# ===== __slots__ Tests =====

def test_dataclass_with_slots():
    instance = DataclassWithSlots()
    
    assert instance.slot_field_a == 1
    assert instance.slot_field_b == 'slot'
    assert instance.slot_field_c == False
    
    # Verify __slots__ is present
    assert hasattr(DataclassWithSlots, '__slots__')


def test_dataclass_with_slots_custom_values():
    instance = DataclassWithSlots(slot_field_a=99, slot_field_b='custom', slot_field_c=True)
    
    assert instance.slot_field_a == 99
    assert instance.slot_field_b == 'custom'
    assert instance.slot_field_c == True


def test_dataclass_with_slots_no_dict():
    """Verify that slotted dataclass doesn't have __dict__"""
    instance = DataclassWithSlots()
    
    assert not hasattr(instance, '__dict__')


# ===== __slots__ with __post_init__ Tests =====

def test_dataclass_with_slots_and_post_init():
    instance = DataclassWithSlotsAndPostInit()
    
    assert instance.x == 3
    assert instance.y == 4
    assert instance.magnitude == 5.0  # sqrt(3^2 + 4^2) = 5


def test_dataclass_with_slots_and_post_init_custom():
    instance = DataclassWithSlotsAndPostInit(x=5, y=12)
    
    assert instance.magnitude == 13.0  # sqrt(5^2 + 12^2) = 13


def test_dataclass_with_slots_and_post_init_no_dict():
    """Verify slots work with __post_init__"""
    instance = DataclassWithSlotsAndPostInit()
    
    assert not hasattr(instance, '__dict__')
    assert hasattr(DataclassWithSlotsAndPostInit, '__slots__')


# ===== Complex Inheritance with Slots Tests =====

def test_dataclass_slots_inheritance():
    instance = DataclassSlotsChild()
    
    assert instance.parent_slot_field == 'parent_slot'
    assert instance.child_slot_field == 99


def test_dataclass_slots_inheritance_custom_values():
    instance = DataclassSlotsChild(parent_slot_field='custom_parent', child_slot_field=42)
    
    assert instance.parent_slot_field == 'custom_parent'
    assert instance.child_slot_field == 42


def test_dataclass_slots_inheritance_no_dict():
    """Verify slots are inherited properly"""
    instance = DataclassSlotsChild()
    
    assert not hasattr(instance, '__dict__')