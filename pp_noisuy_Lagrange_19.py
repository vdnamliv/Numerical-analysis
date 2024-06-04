def lagrange_polynomial(x_data, y_data, x):
  """
  Evaluates the Lagrange polynomial for the given data points at a specific x value.

  Args:
      x_data: A list of data points (x-coordinates).
      y_data: A list of data points (y-coordinates).
      x: The x value at which to evaluate the polynomial.

  Returns:
      The value of the Lagrange polynomial at x.
  """

  n = len(x_data)
  result = 0
  for i in range(n):
    basis = 1
    for j in range(n):
      if i != j:
        basis *= (x - x_data[j]) / (x_data[i] - x_data[j])
    result += basis * y_data[i]
  return result

# Extract data from the image (assuming it's accessible)
# Replace with your data extraction logic based on the image format and content
x_data = [0, 6, 10, 13, 17, 20, 28]  # Replace with actual x-values from the image
y_data = [6.67, 17.33, 42.67, 37.33, 30.10, 29.31, 28.74]  # Replace with actual y-values from the image

# Choose a specific x value for evaluation (e.g., x = 15)
x = 15

# Evaluate the Lagrange polynomial at x
y_interpolated = lagrange_polynomial(x_data, y_data, x)

print(f"Lagrange polynomial interpolation for x = {x}: y = {y_interpolated}")
