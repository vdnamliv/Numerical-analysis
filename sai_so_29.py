import math

# True value of pi
true_pi = math.pi

# Approximations
approx_22_7 = 22 / 7
approx_355_113 = 355 / 113

# Absolute errors
error_22_7 = abs(true_pi - approx_22_7)
error_355_113 = abs(true_pi - approx_355_113)

# Relative errors
relative_error_22_7 = error_22_7 / true_pi
relative_error_355_113 = error_355_113 / true_pi

# Print results with 3 significant digits
print(f"True value of pi: {true_pi:.12f}")
print(f"Approximation 22/7: {approx_22_7:.12f}")
print(f"Approximation 355/113: {approx_355_113:.12f}")

print(f"\nAbsolute error for 22/7: {error_22_7:.12f}")
print(f"Relative error for 22/7: {relative_error_22_7:.3g}")

print(f"\nAbsolute error for 355/113: {error_355_113:.12f}")
print(f"Relative error for 355/113: {relative_error_355_113:.3g}")
