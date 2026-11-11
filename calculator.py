# https://github.com/nanduprav/lab11-NP-AY
# Partner 1: Nandana Praveen
# Partner 2: Angela Yang
# Partner 3: Keysie Perez

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments.")
    return math.log(b, a)


def exponent(a, b):
    return a ** b

def hypotenuse(a, b):
    return math.hypot(a, b)

def square_root(a):
    if a < 0 :
        raise ValueError("Invalid sqrt argument.")
    return math.sqrt(a)

