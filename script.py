import math
import sys
from os import rename
from typing import Any

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    """Greeting with format"""
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


def greet_two(greets: str) -> str:
    """Greet with fstring"""
    greets = f"Hello, {greets}"
    return greets


def greet_three(greeting: str) -> str:
    """Greet with +"""
    greeting = "Hello, " + greeting
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)

"""Faire tourner le code dans le terminal avec les input"""
# name = input("Your name? ")
# print("Hello, ", name)


# def greet
print(greet("World"))
print(greet("Sylvain"))
# def greetTwo
print(greet_two("Universe"))
print(greet_two("Husser"))
# def greetThree
print(greet_three("People"))
print(greet_three("Kana"))
