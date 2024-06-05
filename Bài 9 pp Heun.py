# Bài 9 pp Heun
import numpy as np

def f(t, y):
  # a) t*e^(3*t)-2y
  # return t*np.exp(3*t) - 2*y
  # b) 1+(t-y)^2
  # return 1+(t-y)**2
  # c) 1 + y/t
  # return 1+y/t
  # d) cos(2t) + sin(3t)
  #return np.cos(2*t) + np.sin(3*t)

h = float(input('Nhập h = '))
lower = float(input('Nhập a = '))
upper = float(input('Nhập b = '))
y0 = float(input('Nhập y(%.0f) = ' %lower))
y = [y0]

k = 10  # how many time needed to correct in Heun method
t = np.linspace(lower, upper, int((upper - lower) + 1 / h))

for i in range(len(t) - 1):
  y_predict = y[i] + h*f(t[i], y[i])     # predictor
  y_next = y[i] + 0.5*h*(f(t[i], y[i]) + f(t[i], y_predict))     # corrector
  for _ in range(k-1):
    y_next = y[i] + 0.5*h*(f(t[i], y[i]) + f(t[i], y_next))     # corrector
  y.extend([y_next])

# Format
print("   t     |      y")
print(np.vstack((t, y)).T)