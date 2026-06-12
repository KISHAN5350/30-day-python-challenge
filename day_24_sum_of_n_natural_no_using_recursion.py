

# Experiment 41: Recursive Sum of Natural Numbers


def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)


n = int(input("Enter n: "))

print(f"Sum of first {n} natural numbers = {sum_natural(n)}")