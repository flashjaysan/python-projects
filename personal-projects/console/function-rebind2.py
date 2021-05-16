"""Demonstration of a handmade decorator second version"""


def greeting(name):
    print(f'Hello, {name}.')


greeting('harschnitzel') # prints Hello, harschnitzel.


def greeting_decorator(greeting_func):
    def full_greeting(name):
        print('NEW GREETING:')
        greeting_func(name)
        print('How are you today?')
    return full_greeting


greeting = greeting_decorator(greeting) # rebinds the greeting name to the decorated function
greeting('harschnitzel') # prints Hello, harschnitzel. How are you today?
