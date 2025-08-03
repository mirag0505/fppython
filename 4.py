from pymonad.maybe import Just
from pymonad.list import ListMonad

def add(x):
    return lambda y: x + y

def add10(functor):
    return functor.map(add(10))

print(add10(Just(5)))
print(add10(ListMonad(1, 2, 3, 4)))