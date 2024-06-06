## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd

#Chương 7 - Giải PTVP
#PTVP - Bậc thấp - PP Euler, Taylor2ord, Mid-point, Heun

def euler(y0, t, f):
  y = [y0]
  h = np.diff(t)[0]
  for i in range(t.shape[0]-1):
    y.append(y[i]+h*f(t[i],y[i]))
  return y

def taylor2ord(y0, t, f):
  def df(t, y):
    eps = 1e-6
    return (f(t+eps, y) - f(t, y)) / eps
  y = [y0]
  h = np.diff(t)[0]
  for i in range(t.shape[0]-1):
    y.append(y[i]+h*f(t[i],y[i])+h**2*df(t[i], y[i])/2)
  return y

def midpoint(y0, t, f):
  y = [y0]
  h = np.diff(t)[0]
  for i in range(t.shape[0]-1):
    y1 = y[i] + 0.5*h*f(t[i], y[i])
    t1 = t[i] + 0.5*h
    y2 = y[i] + h*f(t1, y1)
    y.append(y2)
  return y

def heun(y0, t, f, k=5):
  y = [y0]
  h = np.diff(t)[0]
  for i in range(t.shape[0]-1):
    y1 = y[i]+ h*f(t[i], y[i])
    y2 = y1
    for j in range(k):
      y2 = y[i]+ h/2*(f(t[i], y[i]) + f(t[i], y2))
    y.append(y2)
  return y

def plot_fn(y0, t, f, yt=None):
  y = np.zeros_like(t)
  if yt != None:
    y = yt(t)
  y1 = euler(y0, t, f)
  y2 = taylor2ord(y0, t, f)
  y3 = midpoint(y0, t, f)
  y4 = heun(y0, t, f)
  plt.plot(t, y1, color = 'orange', label="Euler Method")
  plt.plot(t, y2, color = 'red', label="Taylor2nd Method")
  plt.plot(t, y3, color = 'blue', label="Midpoint Method")
  plt.plot(t, y4, color = 'green', label="Heun Method")
  if yt != None:
    plt.plot(t, y, color = 'black', label="True value")
  plt.legend()
  plt.xlabel('t')
  plt.ylabel('y')
  plt.title('Đồ thị y(t) sau khi giải phương trình y` = f(t,y)')
  plt.show()
  df = pd.DataFrame({
      't': t,  # Wrap the scalar values in lists
      'true':y,
      'Euler': y1,
      'Taylor-2ord': y2,
      'Mid-Point': y3,
      'Heun': y4
  })
  return df, y, y1, y2, y3, y4

 ## Bài 9 - c7b1, (b, c)
case_ = 'c'
def init(case_):
  if case_ == 'b':
    a, b, y0 = 0, 1, 1
    def f(t,y):
      return -y + t - 1
  elif case_ == 'c':
    a, b, y0 = 0, 1, 1
    def f(t,y):
      return t-np.exp(t)
  else: return None
  return a, b, y0, f

a, b, y0, f = init(case_)
h = 0.1
n = int((b-a)/h)
t = np.linspace(a, b, n+1)
df, y_true, y_euler, y_taylor2, y_midpoint, y_heun = plot_fn(y0, t,f)
df.head()