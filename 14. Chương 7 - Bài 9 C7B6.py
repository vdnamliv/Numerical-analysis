## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd

def rk4(a, b, ic, h, f):
    n = int((b-a)/h)
    t, w = a, np.array(ic)
    tv, x1v, x2v = [], [], []
    for i in range(n):        
        k1 = np.array([h*fi(t, w) for fi in f])        
        k2 = np.array([h*fi(t+h/2, w+k1/2) for fi in f])
        k3 = np.array([h*fi(t+h/2, w+k2/2) for fi in f])
        k4 = np.array([h*fi(t+h, w+k3) for fi in f])        
        w = w + 1/6*(k1 + 2*k2 + 2*k3 + k4)
        t = t + h
        print(i+1, t, w)
        tv.append(t)
        x1v.append(w[0])
        x2v.append(w[1])
    return tv, x1v, x2v    
        
def f1(t, w): return 3*w[0] - 0.002*w[0]*w[1]
def f2(t, w): return 0.0006*w[0]*w[1] - 0.5*w[1]

#### Change 4 to 40 for checking oscillating nature ###
t, x1, x2 = rk4(0, 4, [1000, 500], 0.1, [f1, f2])