import math


def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z


def naiveTime(a):
    steps = 3 + 2 * a
    return steps


def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
    return z


def countDown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print y


def countDownTime(n):
    """ returns the numbers of steps """
    """ print countDown(n) """
    # steps = 3 + 2 * (n / 5 + (n % 5 > 0))
    steps = 3 + 2 * math.ceil(n / 5)
    return steps
