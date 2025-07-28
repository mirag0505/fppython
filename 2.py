from pymonad.tools import curry

# 2.3.1
@curry(2)
def greetingText(str1: str, name: str) -> str:
    return str1 + name

greet = greetingText("Hello, ")
result = greet("Anna")
print(result)

# 2.3.2
@curry(4)
def first_step(greeting_word: str, punctuation: str, ending: str, name: str,) -> str:
    return f"{greeting_word}{punctuation} {name}{ending}"


final = first_step("Hello")(",")("!")
result = final("Petya")
print(result)