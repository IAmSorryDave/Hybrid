from functools import partial, wraps
from inspect import signature
from types import FunctionType

def hybrid(node):
    sig = signature(node)
    param_names = set(sig.parameters.keys())
    
    @wraps(node)
    def wrapper(__class_or_instance = None , /, *args , **kwargs):
        nonlocal node
        copy_of_node = FunctionType(node.__code__, node.__globals__, name=node.__name__, argdefs=node.__defaults__, closure=node.__closure__)
        copy_of_node.__kwdefaults__ = node.__kwdefaults__.copy() if node.__kwdefaults__ is not None else None

        if __class_or_instance is not None:
            injected_kwargs = {}
            has_matching_attrs = False
            
            for key in dir(__class_or_instance):
                if key in param_names:
                    has_matching_attrs = True
                    attribute = getattr(__class_or_instance, key)
                    if isinstance(attribute, FunctionType) and attribute.__code__ == node.__code__:
                        copy_of_node = node
                        break
                    injected_kwargs[key] = attribute
            
            # If no matching attributes, it's a positional arg, not a class/instance
            if not has_matching_attrs:
                args = (__class_or_instance,) + args
                __class_or_instance = None
            elif injected_kwargs:
                copy_of_node = partial(copy_of_node, **injected_kwargs)
        
        return copy_of_node(*args, **kwargs)
    return wrapper