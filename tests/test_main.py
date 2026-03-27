
import pytest

from hybrid import my_function, MyClass, MySubClass, MyDataClass

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