# Experiment 15: Multiplication Tables
for n in [8, 15, 69]:
    print(f"\nMultiplication Table of {n}:")
    
    for i in range(1, 11):
        print(f"{n} x {i:2d} = {n * i}")