## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd

"""## Chương 3 - Giải gần đúng hệ phương trình
#Chương 3 - PP Khử Gauss"""

def gauss_elimination(A, b):
  # Nối ma trận A và vector b thành ma trận mở rộng [A | b]
  n = len(b)
  A_ = np.hstack((A.astype(float), np.expand_dims(b.astype(float), axis=1)))

  # Forward elimination
  for i in range(n):
  # Chọn pivot
    p_ = i
    for j in range(i + 1, n):
      if abs(A_[j, i]) > abs(A_[p_, i]):
        p_ = j
    A_[[p_, i]] = A_[[i, p_]]

  # Loại bỏ phần tử dưới pivot
    for j in range(i + 1, n):
      factor = A_[j, i] / A_[i, i]
      A_[j, i:] -= factor * A_[i, i:]

  # Back substitution
  x = np.zeros(n)
  for i in range(n - 1, -1, -1):
    # if A_[i, i] == 0:
    # 	return
    x[i] = (A_[i, -1] - np.dot(A_[i, i + 1:n], x[i + 1:n])) / A_[i, i]
  return x

#bài 9
def solve_system(a):

  coefficient_matrix = np.array([[2, -6*a], [3*a, -1]])
  constant_vector = np.array([3, 3/2])

  # Check if determinant is zero (infinite solutions or no solution)
  determinant = np.linalg.det(coefficient_matrix)
  if abs(determinant) < 1e-6:
    if np.allclose(coefficient_matrix.dot(constant_vector), np.zeros(2)):
      return (True, np.inf)  # Infinite solutions (vô số nghiệm)
    else:
      return (False, None)  # No solution (vô nghiệm)

  # Solve the system using inverse
  solution = np.linalg.inv(coefficient_matrix).dot(constant_vector)
  return (True, solution)

# Analyze and solve for different values of 'a'
def analyze_and_solve(a_values):
  for a in a_values:
    has_solution, solution = solve_system(a)
    if has_solution:
      if solution is np.inf:
        print(f"For a = {a}: Infinite number of solutions")
      else:
        print(f"For a = {a}: Solution (x1, x2) = {solution}")
    else:
      print(f"For a = {a}: No solution")

a_values = [1, 2, 1/3]  # Test cases for different values of 'a'
analyze_and_solve(a_values)

# Bài 19 - Sử dụng PP Khử Gauss
case_ = 'a'
def Matrix_Ab(case_):
  if case_ == 'a':
    A = np.array([[4, 2, 4, 0],
                  [2, 2, 3, 2],
                  [4, 3, 6, 3],
                  [0, 2, 3, 9]])
    b = np.array([20, 36, 60, 122])
  return A, b
A, b = Matrix_Ab(case_)
res = gauss_elimination(A, b)
if math.isnan(res[0]):
  print("Phương trình vô nghiệm")
elif math.isinf(res[0]):
  print("Phương trình vô số nghiệm")
else:
  print("Nghiệm của hệ phương trình:")
  print(res)