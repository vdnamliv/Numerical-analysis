import numpy as np

def cholesky_solve(A, b):
  """
  Solves a system of linear equations Ax = b using Cholesky decomposition.

  Args:
      A: A square, positive definite coefficient matrix.
      b: The right-hand side vector.

  Returns:
      The solution vector x.
  """

  # Perform Cholesky decomposition (L * L^T = A)
  L = np.linalg.cholesky(A)

  # Forward substitution (Ly = b)
  y = np.linalg.solve(L, b)

  # Backward substitution (Ux = y)
  x = np.linalg.solve(L.T, y)

  return x

# Define the coefficient matrix A and right-hand side vector b
A = np.array([[0.01, 0.0, 0.03],
              [0.0, 0.16, 0.08],
              [0.03, 0.08, 0.14]])
b = np.array([0.14, 0.16, 0.54])

# Check if A is positive definite (required for Cholesky decomposition)
if not np.all(np.linalg.eigvals(A) > 0):
  raise ValueError("Coefficient matrix A is not positive definite")

# Solve the system using Cholesky decomposition
x = cholesky_solve(A, b)

# Print the solution
print("Solution (x1, x2, x3):", x)
