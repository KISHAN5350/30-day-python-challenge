# Experiment 23: Reverse a Number
num = int(input("Enter a number: "))

rev = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed number:", rev)