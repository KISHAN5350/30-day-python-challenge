# Experiment 22: Counting Digits in a Number
num = int(input("Enter a number: "))

count = 0
temp = abs(num)

if temp == 0:
    count = 1

while temp > 0:
    temp //= 10
    count += 1

print("Number of digits in", num, ":", count)