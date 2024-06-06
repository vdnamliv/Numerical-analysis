## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd

"""## Chương 2 - Giải gần đúng phương trình

### Chương 2 - PP Chia đôi
"""

def bisection_method(f, a, b, eps = 1e-5, max_iterations=1000):
	p_old = 0
	for i in range(max_iterations):
		p = (a + b) / 2
		if (f(p) == 0 or np.abs(p - p_old)/ np.abs(p) < eps):
			return p, i
		elif(f(a) * f(p) < 0):
			b = p
		else:
			a = p
		p_old = p
	return p, i

# Bài 9
def f(x):
  return math.e**x - 2 - math.cos(math.e**x - 2)
a1, b1 = 0.5, 1.5

res, iters = bisection_method(f, a1, b1)
print("Nghiệm của phương trình:\n", round(res, 10))
print("Số lần lặp:", iters)

# Bài 19
def f(x):
  return x - math.sin(0.3308 - x * math.sqrt(1 - x**2))
  #sau khi thay L = 10, r = 1 , V = 12.4 và biến đổi, ta được hàm như trên.

a1, b1 = 0, 1 # vì 0 ≤ h ≤ r=1

res, iters = bisection_method(f, a1, b1)

print("Chiều cao h =", res)
print("Số lần lặp:", iters)