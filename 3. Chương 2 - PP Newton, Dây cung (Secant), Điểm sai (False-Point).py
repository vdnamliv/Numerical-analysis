## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd

"""###Chương 2 - PP Newton, Dây cung (Secant), Điểm sai (False-Point)"""

def Newton_method(p0, f, df, eps = 10**-10, max_iterations = 1000000):
	for i in range (max_iterations):
		p = p0 - f(p0)/df(p0)
		if np.abs((f(p)-f(p0))) < eps:
			return p, i
		p0 = p
	return p, i

def Secant_method(f, a, b, eps = 10**-10, max_iterations = 1000000):
  for i in range (max_iterations):
    c = b - f(b)*(b - a) / (f(b) - f(a))
    if np.abs(f(c)) < eps:
        return c, i
    a = b
    b = c
  return c, i

def FalPos_method(f, a, b, eps = 10**-10, max_iterations = 1000000):
  for i in range (max_iterations):
    c = b - f(b)*(b - a) / (f(b) - f(a))
    if f(b) * f(c) < 0: a = b
    b = c
    if np.abs(f(c)) < eps:
      return c, i
  return c, i

# Bài 9
# (em làm cả 3 phương pháp, ví dụ với câu a và câu c Bài 5)
def f(x):
  if case_ == 'a':
    return x**3 - 2*x**2 - 5
  elif case_ == 'c':
    return x - math.cos(x)

def df(x):
  if case_ == 'a':
    return 3*x**2 - 4*x
  elif case_ == 'c':
    return x + math.sin(x)

#case_='c'
#a, b = 0, 0.5*math.pi

case_ = 'a'
a, b = 1, 4

res, iters = Newton_method((a+b)/2, f, df)
print("Theo phương pháp Newton:")
print("Nghiệm xấp xỉ của f(x) là:", round (res,10))
print('Số lần lặp:', iters)

res, iters = Secant_method(f, a, b)
print("\nTheo phương pháp Dây cung:")
print("Nghiệm xấp xỉ của f(x) là:", round (res,10))
print('Số lần lặp:', iters)

res, iters = FalPos_method(f, a, b)
print("\nTheo phương pháp Điểm sai:")
print("Nghiệm xấp xỉ của f(x) là:", round (res,10))
print('Số lần lặp:', iters)