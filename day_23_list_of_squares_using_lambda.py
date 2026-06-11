

# Experiment 43: List of Squares Using Lambda

square = lambda x: x ** 2

numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(square, numbers))

print("Numbers :", numbers)
print("Squares :", squares)
print("Square of 6 =", square(6))