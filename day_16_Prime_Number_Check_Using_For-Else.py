# Experiment 29: Prime Number Check Using For-Else

num = int(input("Enter a number: "))

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print(num, "is Not a Prime number")
        break
else:
    print(num, "is a Prime number")