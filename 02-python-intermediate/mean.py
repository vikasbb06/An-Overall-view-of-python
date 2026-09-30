import math

# Taking input from user
n = int(input("Enter number of values: "))

values = []
for i in range(n):
    num = float(input(f" Enter value {i+1}: "))
    values.append(num)

# Mean
mean = sum(values)/n

# Variance
variance = sum((x - mean)**2 for x in values) / n

# Standard Deviation
std_dev = math.sqrt(variance)

# Output
print("\nResults:")
print("Mean =", mean)
print("Variance =", variance)
print("Standard Deviation =",std_dev)
