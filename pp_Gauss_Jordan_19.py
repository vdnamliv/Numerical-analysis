import numpy as np

def gauss_jordan(A):
  """
  Finds the inverse of a square matrix using Gauss-Jordan elimination.

  Args:
      A: A square matrix.

  Returns:
      The inverse of A, or None if the matrix is singular (not invertible).
  """

  # Check if matrix is square
  if A.shape[0] != A.shape[1]:
    return None

  # Create augmented matrix (combine A and identity matrix)
  n = A.shape[0]
  I = np.eye(n)
  augmented_matrix = np.concatenate((A, I), axis=1)

  # Perform Gauss-Jordan elimination
  for i in range(n):
    # Handle zero pivot (check for singularity)
    if abs(augmented_matrix[i, i]) < 1e-6:
      return None

    # Normalize pivot row
    augmented_matrix[i, :] /= augmented_matrix[i, i]

    # Eliminate elements below pivot
    for j in range(i + 1, n):
      factor = augmented_matrix[j, i]
      augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

  # Back substitution to find inverse
  for i in range(n - 1, -1, -1):
    # Eliminate elements above diagonal
    for j in range(i):
      factor = augmented_matrix[j, i]
      augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

  # Extract inverse matrix
  inverse = augmented_matrix[:, n:]

  return inverse

# Define the coefficient matrix A
A = np.array([[4, 2, 4, 0],
              [2, 2, 3, 2],
              [4, 3, 6, 3],
              [0, 2, 3, 9]])

# Find the inverse
inverse = gauss_jordan(A)

# Check if inverse exists
if inverse is None:
  print("Matrix is singular (not invertible)")
else:
  print("Inverse of A:")
  print(inverse)
