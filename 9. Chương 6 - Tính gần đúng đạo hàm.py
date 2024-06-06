## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd

"""## Chương 6 - Tính gần đúng đạo hàm tích phân

### Chương 6 - Tính gần đúng đạo hàm
"""

def diff3p(X, Y, h):
  dfx = []
  for i in range(X.shape[0]):
    if i==0:
      dfx.append((-3 * Y[i] + 4 * Y[i+1] - Y[i+2]) / (2 * h))
    elif i == X.shape[0]-1:
      dfx.append((-3 * Y[i] + 4 * Y[i-1] - Y[i-2]) / (2 * -h))
    else:
      dfx.append((Y[i+1] - Y[i-1]) / (2 * h))
  return dfx
def diff5p(X, Y, h):
  dfx = []
  for i in range(X.shape[0]):
    if i <= 1:
      dfx.append((-25 * Y[i] + 48 * Y[i+1] - 36 * Y[i+2] + 16 * Y[i+3] - 3 * Y[i+4]) / (12 * h))
    elif i >= X.shape[0]-2:
      dfx.append((-25 * Y[i] + 48 * Y[i-1] - 36 * Y[i-2] + 16 * Y[i-3] - 3 * Y[i-4]) / (12 * -h))
    else:
      dfx.append((Y[i-2] - 8 * Y[i-1] + 8 * Y[i+1] - Y[i+2]) / (12 * h))
  return dfx

## Bài 9
case_ = 'b'
def init(case_):
  if case_ == 'a':
    x = np.array([2.1, 2.2, 2.3, 2.4, 2.5, 2.6])
    y = np.array([-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.601596])
  elif case_ == 'b':
    x = np.array([-3.0, -2.8, -2.6, -2.4, -2.2, -2.0])
    y = np.array([9.367879, 8.233241, 7.180350, 6.209329, 5.320305, 4.51817])
  else: return None
  return x, y
x_, y_ = init(case_)
h = np.diff(x_)[0]
dfx1 = diff3p(x_, y_, h)
# dfx2 = diff5p(x_, y_, h)
print(tabulate(zip(x_, y, dfx1), headers=['X', 'Y', 'dfx3p']))

#Bài 12 (thêm)
case_ = 'a'
def init(case_):
  if case_ == 'a':
    x = np.array([1.05, 1.10, 1.15, 1.20, 1.25, 1.30])
    y = np.array([-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.6015966])
    h = np.diff(x)[0]
    def f(x):
      return np.tan(2*x)
    def df(x):
      return 2*np.tan(2*x)**2+2
  elif case_ == 'b':
    x = np.array([-3.0, -2.8, -2.6, -2.4, -2.2, -2])
    y = np.array([16.08554, 12.64465, 9.863738, 7.623176, 5.825013, 4.389056])
    h = np.diff(x)[0]
    def f(x):
      return np.exp(-x)-1+x
    def df(x):
      return -np.exp(-x)+1
  else: return None
  return x, y, h, f, df

x_, y_, h, f, df = init(case_)
dy_ = df(x_)
dfx1 = diff3p(x_, y_, h)
dfx2 = diff5p(x_, y_, h)

err1 = np.linalg.norm(dy_-dfx1)
err2 = np.linalg.norm(dy_-dfx2)
E1 = np.abs(dy_ - dfx1)
E2 = np.abs(dy_ - dfx2)
print(tabulate(zip(x_, dy_, dfx1, E1, dfx2, E2), headers=['X', 'dY', 'dfx3p', 'err3p', 'dfx5p', 'err5p']))
print("\nSai số của hai phép xấp xỉ đạo hàm là:")
print("\t1. Quy tắc 3 điểm: ", err1)
print("\t2. Quy tắc 5 điểm: ", err2)