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
### Chương 6 - Tính gần đúng tích phân"""

# Hàm comTrapezoidal(Y, a, b) tính tích phân xấp xỉ theo phương pháp hình thang
# - Y: Mảng giá trị hàm số tại các điểm chia đều
# - a: Giới hạn dưới của tích phân
# - b: Giới hạn trên của tích phân
def comTrapezoidal(Y, a, b):
  n = Y.shape[0]  # Lấy số phần tử của mảng Y để tính số đoạn chia
  h = (b-a)/(n-1)  # Tính độ rộng của mỗi đoạn chia
  ifx = (Y[0] + 2*np.sum(Y[1:n-1]) + Y[n-1])*h/2  # Tính tích phân theo công thức hình thang
  return ifx

# Hàm comSimpson(Y, a, b) tính tích phân xấp xỉ theo phương pháp Simpson
# - Y: Mảng giá trị hàm số tại các điểm chia đều
# - a: Giới hạn dưới của tích phân
# - b: Giới hạn trên của tích phân
def comSimpson(Y, a, b):
  n = Y.shape[0]  # Lấy số phần tử của mảng Y để tính số đoạn chia
  h = (b-a)/(n-1)  # Tính độ rộng của mỗi đoạn chia
  ifx = (Y[0] + 4*np.sum(Y[1:n-1:2]) + 2*np.sum(Y[2:n-1:2]) + Y[n-1])*h/3  # Tính tích phân theo công thức Simpson
  return ifx

# Hàm comMidpoint(Y, a, b) tính tích phân xấp xỉ theo phương pháp điểm giữa
# - Y: Mảng giá trị hàm số tại các điểm chia đều
# - a: Giới hạn dưới của tích phân
# - b: Giới hạn trên của tích phân
def comMidpoint(Y, a, b):
  n = Y.shape[0]  # Lấy số phần tử của mảng Y để tính số đoạn chia
  h = (b-a)/(n-1)  # Tính độ rộng của mỗi đoạn chia
  ifx = (2*np.sum(Y[1:n-1:2]))*h  # Tính tích phân theo công thức điểm giữa
  return ifx

# Hàm compareIntApprox(y_, a, b, IntF) so sánh các phương pháp tích phân xấp xỉ
# - y_: Mảng giá trị hàm số tại các điểm chia đều
# - a: Giới hạn dưới của tích phân
# - b: Giới hạn trên của tích phân
# - IntF: Hàm tính tích phân chính xác (dùng để lấy giá trị thực)
def compareIntApprox(y_, a, b, IntF):
  T = comTrapezoidal(y_, a, b)  # Tính tích phân xấp xỉ theo phương pháp hình thang
  S = comSimpson(y_, a, b)    # Tính tích phân xấp xỉ theo phương pháp Simpson
  M = comMidpoint(y_, a, b)   # Tính tích phân xấp xỉ theo phương pháp điểm giữa
  I = IntF(a, b)                # Tính tích phân chính xác bằng hàm IntF

  # Tạo bảng DataFrame để lưu trữ kết quả
  df = pd.DataFrame({
      'True Value': [I, I-I],        # Giá trị thực và Sai số tuyệt đối (gói gọn giá trị đơn trong danh sách)
      'Trapezoidal': [T, T-I],        # Tích phân hình thang và Sai số tuyệt đối
      'Simpson': [S, S-I],          # Tích phân Simpson và Sai số tuyệt đối
      'Mid-Point': [M, M-I]           # Tích phân điểm giữa và Sai số tuyệt đối
  })
  df.index = ['Intergation Value', 'Approximate Error']  # Đặt tên cho các dòng
  return df

  ## Bài 9 - 3 Phương pháp
n = 1000
case_ = 'b'
def init(case_):
  if case_ == 'a':
    a, b = 0.5, 1
    def f(x):
      return x**4
    def intf(x):
      return 4*x**3
  elif case_ == 'b':
    a, b = 0, 0.5
    def f(x):
      return 2/(x-4)
    def intf(x):
      return -2/((x-4)**2)
  elif case_ == 'c':
    a, b = 1, 1.5
    def f(x):
      return (x**2*np.log((abs(x))))
    def intf(x):
      return 2*x*np.log((abs(x))) + x
  else: return None
  return a, b, f, intf
a, b, f, intf = init(case_)
x_ = np.linspace(a, b, n)
y_ = f(x_)
def IntF(a,b):
  return intf(b) - intf(a)
df = compareIntApprox(y_, a, b, IntF)
df