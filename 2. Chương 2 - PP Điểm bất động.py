## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd

"""### Chương 2 - PP Điểm bất động"""

def fixed_point_iteration(g, p0, eps = 1e-10, max_iterations = 100000):
	for i in range (max_iterations):
		p = g(p0)
		if(np.abs(p - p0)/ np.abs(p) < eps):
			return p, i
		p0 = p
	return p, i

# Bài 9 - Điểm bất động
def fixed_point_iteration(guess, eps=1e-4):

  while True:
    new_guess = (guess + 3 / guess) / 2
    if abs(new_guess - guess) < eps:
      return new_guess
    guess = new_guess

# Tìm kết quả
sqrt_3 = fixed_point_iteration(1)

print(f"Giá trị xấp xỉ của √3 là: {sqrt_3:.4f}")