## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd


"""### Chương 3 - A = LU (Bài 9)

#### Chương 3 - Doolittle
"""

def DoolittleFw(L, b):
  n = len(b)
  y = np.zeros(n)
  for i in range(n):
    y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
  return y

def DoolittleBw(U, y):
  n = len(y)
  x = np.zeros(n)
  for i in range(n - 1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
  return x
def doolittle(A, b):
  n = len(A)
  L = np.zeros((n, n))
  U = np.zeros((n, n))

  for k in range(n):
    U[k, k:] = A[k, k:] - np.dot(L[k, :k], U[:k, k:])
    L[k:, k] = (A[k:, k] - np.dot(L[k:, :k], U[:k, k])) / U[k, k]
  y = DoolittleFw(L, b)
  x = DoolittleBw(U, y)
  return L, U, x

A = np.array([[0.01, 0, 0.03],
              [0, 0.16, 0.08],
              [0.03, 0.08, 0.14]])
b = np.array([0.14, 0.16, 0.54])

L, U, x = doolittle(A, b)
print("Ma trận L:")
print(L)
print("\nMa trận U:")
print(U)
print("\nNghiệm của hệ phương trình:")
print(x)

"""#### Chương 3 - Crout """

def CroutFw(L, b):
  n = L.shape[0]
  y = np.zeros(n)

  for i in range(n):
    y[i] = (b[i] - L[i, :i] @ y[:i]) / L[i, i]
  return y

def CroutBw(U, y):
  n = U.shape[0]
  x = np.zeros(n)

  for i in range(n - 1, -1, -1):
    x[i] = (y[i] - U[i, i + 1:] @ x[i + 1:]) / U[i, i]
  return x
def crout(A, b):
  n = A.shape[0]
  L = np.zeros((n, n))
  U = np.zeros((n, n))

  for j in range(n):
    L[j, j] = A[j, j] - L[j, :j] @ U[:j, j]
    U[j, j] = 1
    for i in range(j + 1, n):
      L[i, j] = A[i, j] - L[i, :j] @ U[:j, j]
    for k in range(j + 1, n):
      U[j, k] = (A[j, k] - L[j, :j] @ U[:j, k]) / L[j, j]
  y = CroutFw(L, b)
  x = CroutBw(U, y)
  return L, U, x

A = np.array([[0.01, 0, 0.03],
              [0, 0.16, 0.08],
              [0.03, 0.08, 0.14]])
b = np.array([0.14, 0.16, 0.54])

L, U, x = crout(A, b)
print('Ma trận L:')
print(L)
print('Ma trận U:')
print(U)
print("Nghiệm của hệ phương trình:")
print(x)

"""#### Chương 3 - Cholesky """

def CholeskyFw(L, b):
  n = len(b)
  y = np.zeros(n)

  for i in range(n):
      y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

  return y

def CholeskyBw(L, y):
  n = len(y)
  x = np.zeros(n)

  for i in range(n - 1, -1, -1):
      x[i] = (y[i] - np.dot(L[i, i + 1:], x[i + 1:])) / L[i, i]

  return x
def cholesky(A,b):
  n = len(A)
  L = np.zeros((n, n))

  for i in range(n):
    for j in range(i + 1):
      if i == j:
        L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :i]**2))
      else:
        L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
  y = CholeskyFw(L, b)
  x = CholeskyBw(L.T, y)
  return L, x

#bài 9
A = np.array([[0.01, 0, 0.03],
              [0, 0.16, 0.08],
              [0.03, 0.08, 0.14]])
b = np.array([0.14, 0.16, 0.54])

L, x = cholesky(A, b)
print('Ma trận L:')
print(L)
print("Nghiệm của hệ phương trình:")
print(x)