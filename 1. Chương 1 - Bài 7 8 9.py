## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd

#Bài 7,8,9
# coefficients
a = 1
b = -40
c = 2

# calculate the discriminant
D = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(D))/(2*a)
sol2 = (-b+cmath.sqrt(D))/(2*a)

# round the real and imaginary parts separately
sol1 = round(sol1.real, 6) + round(sol1.imag, 6) * 1j
sol2 = round(sol2.real, 6) + round(sol2.imag, 6) * 1j

print("The solutions are {0} and {1}".format(sol1,sol2))