from random import random


def private_key(p):
    a = random(1 , p-1)
    b = random(1 , p-1)

    return a, b


def public_key(p, g, private):
    private


def secret(p, public, private):
    pass
