import math


def easeInSine(value):
    return 1 - math.cos((value * math.pi) / 2)


def easeOutSine(value):
    return math.sin((value * math.pi) / 2)


def easeInOutSine(value):
    return -(math.cos(math.pi * value) - 1) / 2


def easeInQuad(value):
    return value ** 2


def easeOutQuad(value):
    return 1 - (1 - value) ** 2


def easeInOutQuad(value):
    if value < 0.5:
        return 2 * value ** 2
    else:
        return 1 - (-2 * value + 2) ** 2 / 2


def easeInCubic(value):
    return value ** 3


def easeOutCubic(value):
    return 1 - (1 - value) ** 3


def easeInOutCubic(value):
    if value < 0.5:
        return 4 * value ** 3
    else:
        return 1 - (-2 * value + 2) ** 3 / 2


def easeInQuart(value):
    return value ** 4


def easeOutQuart(value):
    return 1 - (1 - value) ** 4


def easeInOutQuart(value):
    if value < 0.5:
        return 8 * value ** 4
    else:
        return 1 - (-2 * value + 2) ** 4 / 2


def easeInQuint(value):
    return value ** 5


def easeOutQuint(value):
    return 1 - (1 - value) ** 5


def easeInOutQuint(value):
    if value < 0.5:
        return 16 * value ** 5
    else:
        return 1 - (-2 * value + 2) ** 5 / 2


def easeInExpo(value):
    if value == 0:
        return 0
    else:
        return 2 ** (10 * value - 10)


def easeOutExpo(value):
    if value == 1:
        return 1
    else:
        return 1 - 2 ** (-10 * value)


def easeInOutExpo(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    elif value < 0.5:
        return 2 ** (20 * value - 10) / 2
    else:
        return (2 - 2 ** (-20 * value + 10)) / 2


def easeInCirc(value):
    return 1 - math.sqrt(1 - value ** 2)


def easeOutCirc(value):
    return math.sqrt(1 - (value - 1) ** 2)


def easeInOutCirc(value):
    if value < 0.5:
        return (1 - math.sqrt(1 - (2 * value) ** 2)) / 2
    else:
        return (math.sqrt(1 - (-2 * value + 2) ** 2) + 1) / 2


def easeInBack(value):
    return 2.70158 * value ** 3 - 1.70158 * value ** 2


def easeOutBack(value):
    return 1 + 2.70158 * (value - 1) ** 3 + 1.70158 * (value - 1) ** 2


def easeInOutBack(value):
    magic_number = 1.70158 * 1.525

    if value < 0.5:
        return ((2 * value) ** 2 * ((magic_number + 1) * 2 * value - magic_number)) / 2
    else:
        return ((2 * value - 2) ** 2 * ((magic_number + 1) * (value * 2 - 2) + magic_number) + 2) / 2


def easeInElastic(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    else:
        return -(2 ** (10 * value - 10)) * math.sin((value * 10 - 10.75) * 2 * math.pi / 3)


def easeOutElastic(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    else:
        return 2 ** (-10 * value) * math.sin((value * 10 - 0.75) * 2 * math.pi / 3) + 1


def easeInOutElastic(value):
    c5 = 2 * math.pi / 4.5

    if value == 0:
        return 0
    elif value == 1:
        return 1
    elif value < 0.5:
        return -(2 ** (20 * value - 10) * math.sin((20 * value - 11.125) * 2 * math.pi / 4.5)) / 2
    else:
        return (2 ** (-20 * value + 10) * math.sin((20 * value - 11.125) * 2 * math.pi / 4.5)) / 2 + 1


def easeInBounce(value):
    return 1 - easeOutBounce(1 - value)


def easeOutBounce(value):
    if value < 1 / 2.75:
        return 7.5625 * value ** 2
    elif value < 2 / 2.75:
        value -= 1.5 / 2.75
        return 7.5625 * value ** 2 + 0.75
    elif value < 2.5 / 2.75:
        value -= 2.25 / 2.75
        return 7.5625 * value ** 2 + 0.9375
    else:
        value -= 2.625 / 2.75
        return 7.5625 * value ** 2 + 0.984375


def easeInOutBounce(value):
    if value < 0.5:
        return (1 - easeOutBounce(1 - 2 * value)) / 2
    else:
        return (1 + easeOutBounce(2 * value - 1)) / 2
