"""
Global is a better term for this file, but you can't use that as a file name in python :/
"""

import funcy_pipe
from funcy_pipe.chain import Chain

class CallableForwarder:
    def __call__(self, *args, **kwargs):
        # TODO call Chainable
        return Chain(*args, **kwargs)

    # forward access to module
    def __getattr__(self, name):
        return getattr(funcy_pipe, name)
    
# TODO add this to builts like icecream