import math

# Calculate partial sums for e^-x with x = 1
def maclaurin_series_e_neg_x(x, terms):
    partial_sums = []
    for n in range(5, terms+1):
        partial_sum = sum([((-x)**i) / math.factorial(i) for i in range(n)])
        partial_sums.append(partial_sum)
    return partial_sums

# Calculate partial sums for e^x with x = 1 and take the reciprocal
def maclaurin_series_e_x(x, terms):
    partial_sums = []
    for n in range(5, terms+1):
        partial_sum = sum([(x**i) / math.factorial(i) for i in range(n)])
        partial_sums.append(1/partial_sum)
    return partial_sums

# Define the number of terms
terms = 10
x = 1

# Calculate partial sums
partial_sums_e_neg_x = maclaurin_series_e_neg_x(x, terms)
partial_sums_e_x_reciprocal = maclaurin_series_e_x(x, terms)

# True value of 1/e for comparison
true_value = 1 / math.e

# Print results
print("Partial sums of e^-x for x = 1:")
for i, sum_val in enumerate(partial_sums_e_neg_x, start=5):
    print(f"Terms: {i}, Approximation: {sum_val}, Error: {abs(sum_val - true_value)}")

print("\nPartial sums of e^x for x = 1 and taking reciprocal:")
for i, sum_val in enumerate(partial_sums_e_x_reciprocal, start=5):
    print(f"Terms: {i}, Approximation: {sum_val}, Error: {abs(sum_val - true_value)}")

"""
conclusion: 
1. The approximation using the Maclaurin series for e^-1 converges faster 
to the true value compared to the approximation using the reciprocal of the Maclaurin series for e^1
2. The error decreases more significantly with each additional term for the series of e^-1 
compared to the reciprocal series of e^1
"""