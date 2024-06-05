# Bài 9 bình phương xấp xỉ rời rạc
# chọn y = ax + b
import numpy as np
import math
import matplotlib.pyplot as plt

def appf(a,x):
  return a[1] * x + a[0]
def BPTTRR(x, y, n):
    sums = [np.sum(np.fromiter((xi**j for xi in x), dtype=float), dtype=float) for j in range(n*2+1)]
    mtr = np.zeros((n+1,n+1))    
    b = np.zeros((n+1,1))
    for i in range(n+1):
        for j in range(n+1):
            mtr[i,j] = sums[i+j]
    for j in range(n+1):
        b[j,0] = np.sum(np.fromiter((x[i]**j * y[i] for i in range(len(x))), dtype=float)) 
    return np.linalg.solve(mtr, b)
    
data = np.array([[28,3.84],[25,3.21],[28,3.23],
                 [27,3.63],[28,3.75],[33,3.20],
                 [28,3.41],[29,3.38],[23,3.53],
                 [27,2.03],[29,3.75],[28,3.65],
                 [27,3.87],[29,3.75],[21,1.66],
                 [28,3.12],[28,2.96],[26,2.92],
                 [30,3.10],[24,2.81]])
x = data[:, 0]
y = data[:, 1]
a = BPTTRR(x,y,1)
print('+ He so cua da thuc:', np.transpose(a))

plt.figure(figsize=(10,8))
plt.xlabel('ACT Score')
plt.ylabel('Grade-Point Average|')
plt.grid(True)


plt.plot(x, y, "ro", label="Experimental Data")


x_vals = np.linspace(min(x[:]-10), max(x[:]+10), 10)


plt.plot(x_vals, appf(a,x_vals), label="Linear Fit")


plt.legend()
plt.show()
