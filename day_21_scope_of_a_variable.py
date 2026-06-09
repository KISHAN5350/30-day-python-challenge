# Experiment 36: Scope and Lifetime of Variables

x = 100   # Global variable

def local_demo():
    y = 50   # Local variable
    print("Inside function - Local y:", y)
    print("Inside function - Global x:", x)

def modify_global():
    global x
    x = 200
    print("Modified global x:", x)

local_demo()

print("Outside function - Global x:", x)

modify_global()

print("After modify_global - x:", x)