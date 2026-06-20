# Experiment 49: String Reversal

s = input("Enter a string: ")

# Method 1: Slicing
rev1 = s[::-1]
print("Reversed (slicing) :", rev1)

# Method 2: Loop
rev2 = ""

for ch in s:
    rev2 = ch + rev2

print("Reversed (loop) :", rev2)
