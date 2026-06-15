

# Experiment 46: Anagram Check

s1 = input("Enter first string : ").lower().replace(" ", "")
s2 = input("Enter second string: ").lower().replace(" ", "")

if sorted(s1) == sorted(s2):
    print(f'"{s1}" and "{s2}" are Anagrams')
else:
    print(f'"{s1}" and "{s2}" are NOT Anagrams')