

# Experiment 48: Count Vowels in a String

s = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0
found = []

for ch in s:
    if ch in vowels:
        count += 1
        found.append(ch)

print("String :", s)
print("Vowels :", found)
print("Count :", count)