# Bài 9 tính gần đúng đạo hàm hàm số
import numpy as np

def f(x):
  pass
# ý a
x = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6]
f = [-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.601596]
# ý b
#x = [-3.0, -2.8, -2.6, -2.4, -2.2, -2.0]
#f = [9.367879, 8.233241, 7.180350, 6.209329, 5.320305, 4.51817]
df = []
h = x[1] - x[0]
df.extend([0.5*(-3*f[0] + 4*f[1] - f[2])/h])  # diem dau dung 3-point end point

for i in range(1, len(x) - 1):
  df.extend([0.5*(f[i+1] - f[i-1]) / h])   # cac diem giua dung midpoint

df.extend([0.5*(-3*f[-3] + 4*f[-2] - f[-1]) / h])  # diem cuoi dung 3-point end point

print(df)