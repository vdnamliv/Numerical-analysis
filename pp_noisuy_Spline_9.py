import numpy as np

# Define the function
def f(x):
    return x * np.log(x)

# Data points
x_data = np.array([8.3, 8.6])
y_data = f(x_data)

# Derivatives at the endpoints
f_prime_8_3 = 3.116256
f_prime_8_6 = 3.151762

# Number of intervals (n)
n = len(x_data) - 1

# Step size (h)
h = x_data[1] - x_data[0]

# Set up the matrix A and vector B for the system of equations
A = np.zeros((4, 4))
B = np.zeros(4)

# Clamped boundary conditions
A[0, :] = [1, 0, 0, 0]
B[0] = y_data[0]
A[1, :] = [1, h, h**2, h**3]
B[1] = y_data[1]

# First derivatives at the endpoints
A[2, :] = [0, 1, 0, 0]
B[2] = f_prime_8_3
A[3, :] = [0, 1, 2*h, 3*h**2]
B[3] = f_prime_8_6

# Solve the system of equations
coeffs = np.linalg.solve(A, B)

# Extract the coefficients
a0, b0, c0, d0 = coeffs

# Define the spline function
def spline(x):
    return a0 + b0 * (x - x_data[0]) + c0 * (x - x_data[0])**2 + d0 * (x - x_data[0])**3

# Evaluate the spline at specific points (example: midpoint between 8.3 and 8.6)
x_eval = np.linspace(8.3, 8.6, 5)
y_eval = [spline(x) for x in x_eval]

# Print the evaluated points
print(f"Spline evaluated at {x_eval}: {y_eval}")

# Print the spline coefficients for inspection
print("Spline coefficients:")
print(f"a0 = {a0}, b0 = {b0}, c0 = {c0}, d0 = {d0}")
