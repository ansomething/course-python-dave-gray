from math import pi
import sys
import random as rdm
from enum import Enum
import kansas
from rps7 import rock_paper_scissors

print(pi)

for item in dir(rdm):
    print(item)

print("")
print(kansas.capital)
print(kansas.random_fun_fact())

print(__name__)
print(kansas.__name__)
print(rdm.__name__)

print("")

rock_paper_scissors()
