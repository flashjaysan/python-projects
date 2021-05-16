"""Demonstration of a handmade decorator first version"""


def greeting(name):
    print(f'Hello, {name}.')


greeting('harschnitzel') # prints Hello, harschnitzel.
greeting_alt = greeting # creates another variable that bind to the original greeting function to avoid recursion


def full_greeting(name):
    greeting_alt(name) # calls the original greeting function through its other reference
    print('How are you today?')


full_greeting('harschnitzel') # prints Hello, harschnitzel. How are you today?
greeting = full_greeting # changes the behavior to the original greeting function
greeting('harschnitzel') # prints Hello, harschnitzel. How are you today?
