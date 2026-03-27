
from functools import partial, wraps
from types import FunctionType

def hybrid(node):

    @wraps(node)
    def wrapper(__class_or_instance = None , /, *args , **kwargs):

        nonlocal node
        
        copy_of_node = FunctionType(node.__code__, node.__globals__, name=node.__name__, argdefs=node.__defaults__, closure=node.__closure__)

        copy_of_node.__kwdefaults__ = node.__kwdefaults__.copy() if node.__kwdefaults__ is not None else None

        if __class_or_instance is not None:

            for key in dir(__class_or_instance):

                attribute = getattr(__class_or_instance, key)

                if isinstance(attribute, FunctionType) and attribute.__code__ == node.__code__:
                    
                    copy_of_node = node
                    
                    break

                else:

                    try:
                        
                        partial_derivative = partial(copy_of_node, **{key : attribute})

                        copy_of_node = partial_derivative
                    
                    except TypeError:

                        continue
            
        return copy_of_node(*args, **kwargs)

    return wrapper
