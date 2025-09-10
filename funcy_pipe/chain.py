"""
Chain(a).map(lambda n: n + 1).filter(lambda n: n>2).list()
"""

import funcy

# TODO autogen types for this too.
# TODO need list, set, etc methods for this

def partial_second_arg(func, second_arg):
    return lambda a, *args: func(a, second_arg, *args)

def chain_wrap(func):
    return lambda *args: Chain(func(*args))

class Chain:
    def __init__(self, value):
        self.value = value
      
    
    def list(self):
        return list(self.value)
    
    def __getattr__(self, name):
        "forward method calls to the associated method"

        attr = getattr(funcy, name, None)

        if callable(attr):
            # TODO need to the first/second position arugment thing here too
            return chain_wrap(partial_second_arg(attr, self.value))
        
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

# Usage:
# f = Forwarder()
# f.some_method_from_some_module(args)

# Chain(a).map(lambda n: n + 1).filter(lambda n: n>2).list()