## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd

#Bài 9

# Hàm appf(a, x) tính toán giá trị tại x của một đa thức bậc nhất
# được xác định bởi các hệ số a
def appf(a, x):
  return a[1] * x + a[0]

# Hàm BPTTRR(x, y, n) tìm hệ số của đa thức bậc n 
# phù hợp nhất với các điểm dữ liệu (x, y) theo phương pháp BTTB
def BPTTRR(x, y, n):
  # Tính tổng các lũy thừa của từng phần tử trong x theo từng bậc
  # từ 0 đến 2n (n là bậc của đa thức)
  sums = [np.sum(np.fromiter((xi**j for xi in x), dtype=float), dtype=float) for j in range(n*2+1)]
  
  # Khởi tạo ma trận vuông mtr kích thước (n+1)x(n+1) và vector b kích thước (n+1)x1
  # để lưu trữ hệ số của phương trình theo dạng ma trận
  mtr = np.zeros((n+1,n+1))
  b = np.zeros((n+1,1))

  # Điền giá trị vào ma trận mtr theo công thức của phương trình BTTB
  for i in range(n+1):
    for j in range(n+1):
      mtr[i,j] = sums[i+j]

  # Tính tổng tích của từng lũy thừa của phần tử trong x nhân với y
  # theo từng chỉ số
  for j in range(n+1):
    b[j,0] = np.sum(np.fromiter((x[i]**j * y[i] for i in range(len(x))), dtype=float))

  # Giải hệ phương trình được lưu trữ trong ma trận mtr và vector b
  # để tìm hệ số của đa thức
  return np.linalg.solve(mtr, b)

# Dữ liệu điểm ACT và GPA
data = np.array([[28,3.84],[25,3.21],[28,3.23],
                [27,3.63],[28,3.75],[33,3.20],
                [28,3.41],[29,3.38],[23,3.53],
                [27,2.03],[29,3.75],[28,3.65],
                [27,3.87],[29,3.75],[21,1.66],
                [28,3.12],[28,2.96],[26,2.92],
                [30,3.10],[24,2.81]])

# Trích ra cột ACT và GPA từ data
x = data[:, 0]
y = data[:, 1]

# Tìm hệ số của đa thức bậc 1 phù hợp nhất với dữ liệu
a = BPTTRR(x,y,1)

# In ra hệ số của đa thức được tìm thấy
print('+ He so cua da thuc:', np.transpose(a))

# Khởi tạo biểu đồ với kích thước 10x8
plt.figure(figsize=(10,8))

# Thiết lập nhãn cho trục hoành và trục tung
plt.xlabel('ACT Score')
plt.ylabel('Grade-Point Average|')

# Bật lưới trên biểu đồ
plt.grid(True)

# Vẽ các điểm dữ liệu thực nghiệm
plt.plot(x, y, "ro", label="Experimental Data")

# Tạo các giá trị x để dự đoán theo hàm appf
x_vals = np.linspace(min(x[:]-10), max(x[:]+10), 10)

# Vẽ đường cong dự đoán theo hàm appf với hệ số a tìm được
plt.plot(x_vals, appf(a,x_vals), label="Linear Fit")

# Hiển thị chú thích cho các đường cong
plt.legend()

# Hiển thị biểu đồ
plt.show()