from pymonad.tools import curry
from pymonad.maybe import Just, Nothing
from pymonad.list import ListMonad

@curry(2)
def add(x, y):
    return x + y

def add10(functor):
    return functor.map(add(10))

print(add10(Just(5)))
print(add10(ListMonad(1, 2, 3, 4)))
print(add10(Nothing))