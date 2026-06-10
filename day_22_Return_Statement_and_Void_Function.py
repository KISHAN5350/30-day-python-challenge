

# Experiment 35: Return Statement and Void Function

def square(n):  # Returns value
    return n * n

def display(msg):  # Void function (no return)
    print("Message:", msg)

num = int(input("Enter a number: "))

result = square(num)
print("Square of", num, "=", result)

display("This is a void function example")