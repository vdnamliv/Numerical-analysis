## Import libs
import numpy as np
from scipy.linalg import lu
import random
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate
import pandas as pd

"""### Chương 3 - Giải gián tiếp 

#### Chương 3 - Lặp Jacobi """

#bài 9
def is_diagonally_dominant(A):
  D = np.diag(np.abs(A))  # Đường chéo chính của A
  S = np.sum(np.abs(A), axis=1) - D  # Tổng các phần tử không thuộc đường chéo
  return np.all(D > S)

def jacobi(A, b, eps=1e-10, max_iterations=1000):
  if not is_diagonally_dominant(A):
    print("Cảnh báo: Ma trận không chéo trội. Phương pháp có thể không hội tụ.")
  else:
    for i in range(A.shape[0]):
      p = A[i,i]
      A[i,:] = A[i,:] / p
      b[i] /= p
  n = A.shape[0]
  x = b.copy()
  I = np.eye(n)
  x_ = x
  for k in range(max_iterations):
    x_ = b + (I-A)@x
    if(np.linalg.norm(x_ - x) < eps):
      return x, k
    x = x_
  return x, k

A = np.array([[5, 1, 2],
              [1, 4, -2],
              [2, 3, 8]], dtype=np.float64)
b = np.array([19, -2, -39], dtype=np.float64)

res, iters = jacobi(A, b)
print("Nghiệm của hệ phương trình: \n", res)
print('Số bước lặp: ', iters)

"""#### Chương 3 - Lặp Gauss-Seidel """

#bài 9
from numpy.linalg import inv
def is_diagonally_dominant(A):
  D = np.diag(np.abs(A))  # Đường chéo chính của A
  S = np.sum(np.abs(A), axis=1) - D  # Tổng các phần tử không thuộc đường chéo
  return np.all(D > S)

def Gauss_Seidel(A, b, eps=1e-10, max_iterations=1000):
  if not is_diagonally_dominant(A):
    print("Cảnh báo: Ma trận không chéo trội. Phương pháp có thể không hội tụ.")
  else:
    for i in range(A.shape[0]):
      p = A[i,i]
      A[i,:] = A[i,:] / p
      b[i] /= p

  x = b.copy()
  x_ = x
  I = np.eye(A.shape[0])
  L, D, U = np.tril(A,k=-1), np.diag(np.diag(A)), np.triu(A, k=1)
  for k in range(max_iterations):
    x_ = -inv(I + L) @ U @ x + inv(I + L) @ b
    if(np.linalg.norm(x_ - x) < eps):
      return x, k
    x = x_
  return x, k

A = np.array([[5, 1, 2],
              [1, 4, -2],
              [2, 3, 8]], dtype=np.float64)
b = np.array([19, -2, -39], dtype=np.float64)

res, iters = Gauss_Seidel(A, b)
print("Nghiệm của hệ phương trình: \n", np.round (res,10))
print('Số bước lặp: ', iters)