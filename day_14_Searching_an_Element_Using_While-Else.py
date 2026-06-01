# Experiment 30: Searching an Element Using While-Else

lst = [10, 20, 30, 40]
target = int(input("Enter element to search: "))

i = 0
while i < len(lst):
    if lst[i] == target:
        print("Element", target, "found at index", i)
        break
    i += 1
else:
    print("Element not found")