import numpy as np

def newton_forward_difference(x_data, y_data, x):
  """
  Performs Newton's forward difference interpolation.

  Args:
      x_data: A list of data points (x-coordinates).
      y_data: A list of data points (y-coordinates).
      x: The x value at which to interpolate.

  Returns:
      The interpolated y value using Newton's forward difference formula.
  """

  n = len(x_data)
  u = (x - x_data[0]) / (x_data[1] - x_data[0])  # Normalized distance from first point

  # Forward differences table
  delta = [[0] * n for _ in range(n)]
  for i in range(n):
    delta[i][0] = y_data[i]
  for j in range(1, n):
    for i in range(n - j):
      delta[i][j] = delta[i + 1][j - 1] - delta[i][j - 1]

  # Interpolate using forward differences
  y_interpolated = delta[0][0]
  for i in range(1, n):
    y_interpolated += delta[0][i] * u**i / np.math.factorial(i)

  return y_interpolated

def newton_backward_difference(x_data, y_data, x):
  """
  Performs Newton's backward difference interpolation.

  Args:
      x_data: A list of data points (x-coordinates).
      y_data: A list of data points (y-coordinates).
      x: The x value at which to interpolate.

  Returns:
      The interpolated y value using Newton's backward difference formula.
  """

  n = len(x_data)
  i = n - 1  # Start from the last data point
  u = (x - x_data[i]) / (x_data[i] - x_data[i - 1])  # Normalized distance from last point

  # Backward differences table
  delta = [[0] * n for _ in range(n)]
  for i in range(n):
    delta[i][0] = y_data[i]
  for j in range(1, n):
    for i in range(n - j):
      delta[i][j] = delta[i][j - 1] - delta[i + 1][j - 1]

  # Interpolate using backward differences
  y_interpolated = delta[i][0]
  for j in range(1, n):
    y_interpolated += delta[i][j] * u**j / np.math.factorial(j)

  return y_interpolated

# Data points from the image (assuming x-values are in increasing order)
x_data = [0, 0.2, 0.4, 0.6, 0.8, 1.0]  # Replace with your actual data
y_data = [1.0000, 1.2214, 1.4918, 1.8221, 2.2255, 2.7089]  # Replace with your actual data

# a) Approximate f(0.05) using Newton's forward difference formula
x = 0.05
y_interpolated_forward = newton_forward_difference(x_data, y_data, x)
print(f"a) Newton's forward difference for x = {x}: y ≈ {y_interpolated_forward}")

# b) Approximate f(0.65) using Newton's backward difference formula
x = 0.65
y_interpolated_backward = newton_backward_difference(x_data, y_data, x)
print(f"b) Newton's backward difference for x = {x}: y ≈ {y_interpolated_backward}")

# c) Approximate f(0.43) using Stirling's formula (clarification)
print("c) Explanation:")
print("Stirling's formula is typically used to approximate factorials, not function values directly.")
print("We can use interpolation methods like those above or other techniques for function approximation.")
