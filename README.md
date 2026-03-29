# hybrid 🦎

A Python decorator that enables **polymorphic function behavior** — write a function once, use it everywhere. ✨

## What It Does

The `@hybrid` decorator transforms a single function into a chameleonic entity that seamlessly works as:
- ✅ Standalone functions
- ✅ Instance methods (with state binding)
- ✅ Class methods (with class attributes)
- ✅ Static methods (pure functions)
- ✅ Bare methods (manual control)

All while **automatically injecting class/instance attributes** as keyword arguments when parameters match.

## Installation

```bash
# install from PyPI
pip install hybrid

# alternatively, install the latest pre-release from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --upgrade --no-deps hybrid
```

## Quick Example

```python
from hybrid import hybrid

@hybrid
def greet(*args, greeting='Hello', enthusiasm='!', **kwargs):
    return locals()

# 1. As a standalone function
result = greet('Alice')
# → {'args': ('Alice',), 'greeting': 'Hello', 'enthusiasm': '!', 'kwargs': {}}

# 2. As a method (binds class attributes)
class Greeter:
    greeting = 'Hi'
    enthusiasm = '!!!'
    
    say = greet  # Assign directly!

g = Greeter()
result = g.say('Bob')
# → {'args': ('Bob',), 'greeting': 'Hi', 'enthusiasm': '!!!', 'kwargs': {}}

# 3. With overrides
result = g.say('Charlie', greeting='Hey')
# → {'args': ('Charlie',), 'greeting': 'Hey', 'enthusiasm': '!!!', 'kwargs': {}}
```

## Features

### 🎯 Automatic Attribute Binding
When called on an instance/class, the decorator scans for attributes matching your function's parameter names and injects them as defaults:

```python

@hybrid
def execute(*args, timeout=5, retries=1, **kwargs):
    return locals().copy()

class Config:
    timeout = 30
    retries = 3

    execute = execute

cfg = Config()
result = cfg.execute('task')
# → timeout=30, retries=3 (bound from class attributes!)
```

### 🔄 Works with All Method Types
```python

@hybrid
def standalone_call(*args, value=0, **kwargs):
    return locals()

class MyClass:
    value = 42
    
    my_method = standalone_call  # Instance method
    my_class_method = classmethod(standalone_call)  # Class method
    my_static_method = staticmethod(standalone_call)  # Static method
```

### � Computed Properties
Because `@hybrid` preserves descriptor behavior, you can also use it with `property()` to expose computed, bound values.

```python
from hybrid import hybrid

@hybrid
def compute(*args, factor=2, name='default', **kwargs):
    return locals()

class Example:
    factor = 5
    name = 'example'
    computed = property(compute)

instance = Example()
result = instance.computed
# -> {'args': (), 'factor': 5, 'name': 'example', 'kwargs': {}}

class SubExample(Example):
    name = 'subexample'

sub_result = SubExample().computed
# -> {'args': (), 'factor': 5, 'name': 'subexample', 'kwargs': {}}
```

### �📍 Inheritance Support
Subclass attributes automatically override parent values:

```python
class Parent:
    name = 'Parent'
    
    get_info = hybrid(lambda *a, name='Unknown', **k: locals())

class Child(Parent):
    name = 'Child'

Child().get_info()
# → {'name': 'Child', ...} (inherited and overridden!)
```

### 💾 Dataclass Compatibility
Works seamlessly with dataclasses of all flavors:

```python
from dataclasses import dataclass

@hybrid
def connect(*args, host='0.0.0.0', port=3000, **kwargs):
    return locals()

@dataclass
class Config:
    host: str = 'localhost'
    port: int = 8080

    connect = connect

cfg = Config(host='example.com', port=443)
result = connect('client', ...)  # Positional args work!
```

## Testing

Comprehensive test suite covering:
- ✅ Positional and keyword arguments
- ✅ All method types (instance, class, static, bare)
- ✅ Inheritance and subclasses
- ✅ Dataclass variations (required/optional fields, post_init, inheritance)
- ✅ Slotted dataclasses
- ✅ 25+ test cases

## Why Use It?

1. **DRY** — Define business logic once, use it in multiple contexts
2. **Flexible** — One function, countless ways to call it
3. **Pythonic** — Leverages standard decorator and descriptor protocols
4. **Testable** — Pure functions that work as methods
5. **Type-Safe** — Full keyword argument binding with defaults

## How It Works

The decorator creates a wrapper that:
1. Checks if called on an object (instance/class) or standalone
2. Inspects the object for attributes matching function parameters
3. Creates a partial function binding those attributes as kwargs
4. Preserves positional and additional keyword arguments
5. Returns the result transparently

## License

MIT
