def fixed_point_iteration(guess, tolerance=1e-4):
  """
  Finds an approximation to the square root of a number using fixed-point iteration.

  Args:
      guess: An initial guess for the square root.
      tolerance: The desired accuracy of the approximation.

  Returns:
      An approximation to the square root of the number, accurate to within the tolerance.
  """
  while True:
    new_guess = (guess + 3 / guess) / 2
    if abs(new_guess - guess) < tolerance:
      return new_guess
    guess = new_guess

# Find the square root of 3
sqrt_3 = fixed_point_iteration(1)

# Print the result
print(f"Square root of 3 (approximation): {sqrt_3:.4f}")
