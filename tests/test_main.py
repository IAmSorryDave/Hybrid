from hybridz import my_function, MyClass, MySubClass, MyDataClass


def test_my_function():

    function_namespace = my_function()

    function_variables = function_namespace.keys()

    assert "c" in function_variables
    assert "d" in function_variables
    assert "z" in function_variables
    assert function_namespace["c"] == 2
    assert function_namespace["d"] == "baz"
    assert function_namespace["z"] is False


def test_my_bare_method():

    bare_method_namespace = MyClass.my_bare_method()

    bare_method_variables = bare_method_namespace.keys()

    assert "c" in bare_method_variables
    assert "d" in bare_method_variables
    assert "z" in bare_method_variables
    assert bare_method_namespace["c"] == 2
    assert bare_method_namespace["d"] == "baz"
    assert bare_method_namespace["z"] is False


def test_my_method():

    my_instance = MyClass()

    method_namespace = my_instance.my_method()

    method_variables = method_namespace.keys()

    assert "c" in method_variables
    assert "d" in method_variables
    assert "z" in method_variables
    assert method_namespace["c"] == 2
    assert method_namespace["d"] == "baz"
    assert method_namespace["z"] is True


def test_my_class_method():

    class_method_namespace = MyClass.my_class_method()

    class_method_namespace.keys()

    assert "c" in class_method_namespace
    assert "d" in class_method_namespace
    assert "z" in class_method_namespace
    assert class_method_namespace["c"] == 2
    assert class_method_namespace["d"] == "baz"
    assert class_method_namespace["z"] is True


def test_my_static_method():

    static_method_namespace = MyClass.my_static_method()

    static_method_namespace.keys()

    assert "c" in static_method_namespace
    assert "d" in static_method_namespace
    assert "z" in static_method_namespace
    assert static_method_namespace["c"] == 2
    assert static_method_namespace["d"] == "baz"
    assert static_method_namespace["z"] is False


def test_my_property():

    my_instance = MyClass()

    property_namespace = my_instance.my_property

    assert "c" in property_namespace
    assert "d" in property_namespace
    assert "z" in property_namespace
    assert property_namespace["c"] == 2
    assert property_namespace["d"] == "baz"
    assert property_namespace["z"] is True


def test_my_property_in_subclass():

    my_instance = MySubClass()

    property_namespace = my_instance.my_property

    assert "c" in property_namespace
    assert "d" in property_namespace
    assert "z" in property_namespace
    assert property_namespace["c"] == 2
    assert property_namespace["d"] == "qux"
    assert property_namespace["z"] is True


def test_my_method_in_subclass():

    my_instance = MySubClass()

    method_namespace = my_instance.my_method()

    method_variables = method_namespace.keys()

    assert "c" in method_variables
    assert "d" in method_variables
    assert "z" in method_variables
    assert method_namespace["c"] == 2
    assert method_namespace["d"] == "qux"
    assert method_namespace["z"] is True


def test_my_classmethod_in_subclass():

    class_method_namespace = MySubClass.my_class_method()

    class_method_namespace.keys()

    assert "c" in class_method_namespace
    assert "d" in class_method_namespace
    assert "z" in class_method_namespace
    assert class_method_namespace["c"] == 2
    assert class_method_namespace["d"] == "qux"
    assert class_method_namespace["z"] is True


def test_my_static_method_in_subclass():

    static_method_namespace = MySubClass.my_static_method()

    static_method_namespace.keys()

    assert "c" in static_method_namespace
    assert "d" in static_method_namespace
    assert "z" in static_method_namespace
    assert static_method_namespace["c"] == 2
    assert static_method_namespace["d"] == "baz"
    assert static_method_namespace["z"] is False


def test_my_bare_method_in_subclass():

    bare_method_namespace = MySubClass.my_bare_method()

    bare_method_variables = bare_method_namespace.keys()

    assert "c" in bare_method_variables
    assert "d" in bare_method_variables
    assert "z" in bare_method_variables
    assert bare_method_namespace["c"] == 2
    assert bare_method_namespace["d"] == "baz"
    assert bare_method_namespace["z"] is False


# Tests with single positional argument
def test_my_function_with_positional_arg():
    function_namespace = my_function("arg1")

    assert "args" in function_namespace
    assert function_namespace["args"] == ("arg1",)
    assert function_namespace["c"] == 2
    assert function_namespace["d"] == "baz"
    assert function_namespace["z"] is False


def test_my_function_with_multiple_positional_args():
    function_namespace = my_function("arg1", "arg2", "arg3")

    assert "args" in function_namespace
    assert function_namespace["args"] == ("arg1", "arg2", "arg3")
    assert function_namespace["c"] == 2
    assert function_namespace["d"] == "baz"
    assert function_namespace["z"] is False


# Tests for methods with positional arguments
def test_my_method_with_positional_arg():
    my_instance = MyClass()
    method_namespace = my_instance.my_method("arg1")

    assert "args" in method_namespace
    assert method_namespace["args"] == ("arg1",)
    assert method_namespace["c"] == 2
    assert method_namespace["d"] == "baz"
    assert method_namespace["z"] is True


def test_my_method_with_multiple_positional_args():
    my_instance = MyClass()
    method_namespace = my_instance.my_method("arg1", "arg2")

    assert "args" in method_namespace
    assert method_namespace["args"] == ("arg1", "arg2")
    assert method_namespace["c"] == 2
    assert method_namespace["d"] == "baz"
    assert method_namespace["z"] is True


# Tests for class methods with positional arguments
def test_my_class_method_with_positional_arg():
    class_method_namespace = MyClass.my_class_method("arg1")

    assert "args" in class_method_namespace
    assert class_method_namespace["args"] == ("arg1",)
    assert class_method_namespace["c"] == 2
    assert class_method_namespace["d"] == "baz"
    assert class_method_namespace["z"] is True


def test_my_class_method_with_multiple_positional_args():
    class_method_namespace = MyClass.my_class_method("arg1", "arg2", "arg3")

    assert "args" in class_method_namespace
    assert class_method_namespace["args"] == ("arg1", "arg2", "arg3")
    assert class_method_namespace["c"] == 2
    assert class_method_namespace["d"] == "baz"
    assert class_method_namespace["z"] is True


# Tests for static methods with positional arguments
def test_my_static_method_with_positional_arg():
    static_method_namespace = MyClass.my_static_method("arg1")

    assert "args" in static_method_namespace
    assert static_method_namespace["args"] == ("arg1",)
    assert static_method_namespace["c"] == 2
    assert static_method_namespace["d"] == "baz"
    assert static_method_namespace["z"] is False


def test_my_static_method_with_multiple_positional_args():
    static_method_namespace = MyClass.my_static_method("arg1", "arg2")

    assert "args" in static_method_namespace
    assert static_method_namespace["args"] == ("arg1", "arg2")
    assert static_method_namespace["c"] == 2
    assert static_method_namespace["d"] == "baz"
    assert static_method_namespace["z"] is False


# Tests for bare methods with positional arguments
def test_my_bare_method_with_positional_arg():
    bare_method_namespace = MyClass.my_bare_method("arg1")

    assert "args" in bare_method_namespace
    assert bare_method_namespace["args"] == ("arg1",)
    assert bare_method_namespace["c"] == 2
    assert bare_method_namespace["d"] == "baz"
    assert bare_method_namespace["z"] is False


# Tests for subclass methods with positional arguments
def test_my_method_in_subclass_with_positional_arg():
    my_instance = MySubClass()
    method_namespace = my_instance.my_method("arg1", "arg2")

    assert "args" in method_namespace
    assert method_namespace["args"] == ("arg1", "arg2")
    assert method_namespace["c"] == 2
    assert method_namespace["d"] == "qux"  # From subclass
    assert method_namespace["z"] is True


def test_my_classmethod_in_subclass_with_positional_arg():
    class_method_namespace = MySubClass.my_class_method("arg1")

    assert "args" in class_method_namespace
    assert class_method_namespace["args"] == ("arg1",)
    assert class_method_namespace["c"] == 2
    assert class_method_namespace["d"] == "qux"  # From subclass


def test_my_static_method_in_subclass_with_positional_arg():
    static_method_namespace = MySubClass.my_static_method("arg1")

    assert "args" in static_method_namespace
    assert static_method_namespace["args"] == ("arg1",)
    assert static_method_namespace["c"] == 2
    assert static_method_namespace["d"] == "baz"  # From parent class


# Tests with mixed positional and keyword arguments
def test_my_function_with_positional_and_keyword_args():
    function_namespace = my_function("arg1", "arg2", c=5, d="custom")

    assert "args" in function_namespace
    assert function_namespace["args"] == ("arg1", "arg2")
    assert function_namespace["c"] == 5
    assert function_namespace["d"] == "custom"
    assert function_namespace["z"] is False


def test_my_method_with_positional_and_keyword_args():
    my_instance = MyClass()
    method_namespace = my_instance.my_method("arg1", z=False)

    assert "args" in method_namespace
    assert method_namespace["args"] == ("arg1",)
    assert method_namespace["c"] == 2
    assert method_namespace["d"] == "baz"
    assert method_namespace["z"] is False  # Override from class


def test_my_dataclass_method_with_positional_and_keyword_args():
    dataclass_instance = MyDataClass()
    method_namespace = dataclass_instance.my_method("arg1", c=10, z=False)

    assert "args" in method_namespace
    assert method_namespace["args"] == ("arg1",)
    assert method_namespace["c"] == 10  # Override from dataclass
    assert method_namespace["d"] == "baz"
    assert method_namespace["z"] is False  # Override from dataclass


def test_my_dataclass_property_with_positional_and_keyword_args():
    dataclass_instance = MyDataClass()
    property_namespace = dataclass_instance.my_property

    assert "c" in property_namespace
    assert "d" in property_namespace
    assert "z" in property_namespace
    assert property_namespace["c"] == 3  # From dataclass
    assert property_namespace["d"] == "baz"
    assert property_namespace["z"] is True  # From dataclass
