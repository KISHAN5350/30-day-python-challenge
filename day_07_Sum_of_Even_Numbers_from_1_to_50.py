# Experiment 11: Sum of Even Numbers from 1 to 50
total = 0
print("Even numbers from 1 to 50:")

for i in range(2, 51, 2):
    print(i, end=" ")
    total += i


print("\nSum of even numbers:", total)