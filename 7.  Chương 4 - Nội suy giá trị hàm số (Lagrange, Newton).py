## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd


"""## Chương 4 - Nội suy giá trị hàm số

### Nội suy Lagrange"""

def Lk(x, x_, k=0, eps=1e-6):
  num, den = 1, 1
  for xi in x_:
    if xi != x_[k]:
      num *= (x-xi)
      den *= (x_[k] - xi)
  return num/(den + eps)
def larange_interpolate(fx, x0, x_):
  p = 0
  for k in range(x_.shape[0]):
    lk = Lk(x0, x_, k)
    p += fx[k]*lk
  return p

#bài 9
from sympy import symbols, simplify, expand

# Định nghĩa biến
x = symbols('x')

# Định nghĩa các điểm dữ liệu
x0, y0 = 0, 0
x1, y1 = 0.5, symbols('y')  # y là biến cần tìm
x2, y2 = 1, 3
x3, y3 = 2, 2

# Tính các đa thức Lagrange cơ sở
L0 = (x - x1)*(x - x2)*(x - x3) / ((x0 - x1)*(x0 - x2)*(x0 - x3))
L1 = (x - x0)*(x - x2)*(x - x3) / ((x1 - x0)*(x1 - x2)*(x1 - x3))
L2 = (x - x0)*(x - x1)*(x - x3) / ((x2 - x0)*(x2 - x1)*(x2 - x3))
L3 = (x - x0)*(x - x1)*(x - x2) / ((x3 - x0)*(x3 - x1)*(x3 - x2))

# Tạo đa thức nội suy
P3 = y0*L0 + y1*L1 + y2*L2 + y3*L3
P3 = simplify(P3)

# Tìm hệ số của x^3 trong đa thức P3
P3_expanded = expand(P3)
coeff_x3 = P3_expanded.coeff(x, 3)

# Giải phương trình coeff_x3 = 6 để tìm y
from sympy import solve

y_value = solve(coeff_x3 - 6, y1)[0]
print("Giá trị của y là:")
y_value

# Bài 2 (thêm)
x_ = np.array([0, 0.6, 0.9])
x0 = 0.45
case_ = 'a'
def f(x):
  if case_ == 'a':
    return np.sin(np.pi*x)
  elif case_ == 'b':
    return (x-1)**(1/3)
  elif case_ == 'c':
    return np.log10(3*x-1)
  elif case_ == 'd':
    return np.exp(2*x)-x
  else: return None
fx = f(x_)
res = larange_interpolate(fx, x0, x_)
E = np.abs(f(x0) - res)
print(f"Giá trị nội suy tại x = {x0} là y = {res:.4f}")
print(f'Error = {E:.10f}')

"""### Nội suy Newton"""

def coef(r, k):
  coef = []
  for i in range(k):
    c = 1
    for j in range(i):
      c *= (r-j)/(j+1)
    coef.append(c)
  return np.array(coef)
def diff_interpolation(fx, x_, x0):
  n = len(x_)
  h = x_[1] - x_[0]
  r = (x0 - x_[0])/h
  dif = np.zeros([n, n])
  dif[:,0] = fx
  c = coef(x0, n)

  for j in range(1, n):
    for i in range(n-j):
      dif[i][j] = dif[i+1][j-1] - dif[i][j-1]
  res = 0
  for i in range(n):
    res += c[i]*dif[0, i]
  return res

# Bài 9
case_ = 'a'

def fx(case_):
  if case_ == 'a':
    x0 = 0.05
    x_ = np.array([0, 0.2, 0.4, 0.6, 0.8]) # Removed extra 0
    f_ = np.array([1, 1.2214, 1.49182, 1.82212, 2.22554])
  elif case_ == 'b':
    x0 = 0.65
    x_ = np.array([0, 0.2, 0.4, 0.6, 0.8])
    f_ = np.array([1, 1.2214, 1.49182, 1.82212, 2.22554])
  else:
    return None # Changed to return None instead of Non
  return x0, x_, f_

x0, x_, f_ = fx(case_)
res = diff_interpolation(f_, x_, x0)

print(f"Giá trị nội suy tại x = {x0} là y = {res:.4f}")

# Nội suy Spline
def f(x):
    return x * np.log(x)

# Các điểm dữ liệu
x_data = np.array([8.3, 8.6])
y_data = f(x_data)

# Đạo hàm tại các điểm cuối
f_prime_8_3 = 3.116256
f_prime_8_6 = 3.151762

# Số lượng khoảng (n)
n = len(x_data) - 1

# Kích thước bước (h)
h = x_data[1] - x_data[0]

# Thiết lập ma trận A và vector B cho hệ phương trình
A = np.zeros((4, 4))
B = np.zeros(4)

# Điều kiện biên ép
A[0, :] = [1, 0, 0, 0]
B[0] = y_data[0]
A[1, :] = [1, h, h**2, h**3]
B[1] = y_data[1]

# Đạo hàm bậc nhất tại các điểm cuối
A[2, :] = [0, 1, 0, 0]
B[2] = f_prime_8_3
A[3, :] = [0, 1, 2*h, 3*h**2]
B[3] = f_prime_8_6

# Giải hệ phương trình
coeffs = np.linalg.solve(A, B)

# Trích xuất các hệ số
a0, b0, c0, d0 = coeffs

# Làm tròn các hệ số spline
a0 = round(a0, 6)
b0 = round(b0, 6)
c0 = round(c0, 6)
d0 = round(d0, 6)

# Định nghĩa hàm spline
def spline(x):
    return a0 + b0 * (x - x_data[0]) + c0 * (x - x_data[0])**2 + d0 * (x - x_data[0])**3

# Đánh giá spline tại các điểm cụ thể (ví dụ: điểm giữa 8.3 và 8.6)
x_eval = np.linspace(8.3, 8.6, 5)
y_eval = [spline(x) for x in x_eval]

y_eval_rounded = [round(y, 6) for y in y_eval]

# In các điểm đã đánh giá
print(f"Spline evaluated at {x_eval}: {y_eval_rounded}")

# In các hệ số spline để kiểm tra
print("Spline coefficients:")
print(f"a0 = {a0}, b0 = {b0}, c0 = {c0}, d0 = {d0}")