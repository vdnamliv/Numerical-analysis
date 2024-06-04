import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
  """
  Solves a linear system Ax = b using Gauss-Seidel iteration.

  Args:
      A: The coefficient matrix.
      b: The right-hand side vector.
      x0: The initial guess vector.
      tol: The tolerance for convergence (default: 1e-6).
      max_iter: The maximum number of iterations (default: 100).

  Returns:
      The solution vector x, or None if convergence is not achieved.
  """

  n = len(b)
  x = x0.copy()
  for _ in range(max_iter):
    for i in range(n):
      # Update x_i using the latest values of other variables (6S method)
      sum_j = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
      x[i] = (b[i] - sum_j) / A[i, i]

    # Check convergence
    if np.linalg.norm(x - x0) < tol:
      return x
    x0 = x.copy()

  print("Convergence not achieved after", max_iter, "iterations.")
  return None

# Define the coefficient matrix A and right-hand side vector b
A = np.array([[5, 1, 2], [1, 4, -2], [2, 3, 8]])
b = np.array([19, -2, 39])

# Initial guess vector
x0 = np.array([1, 1, 1])

# Perform 5 steps of Gauss-Seidel iteration
solution = gauss_seidel(A, b, x0, max_iter=5)

if solution is not None:
  print("Solution after 5 iterations:")
  print(solution)
