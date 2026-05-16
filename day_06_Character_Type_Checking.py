# Experiment 8: Character Type Checking
ch = input("Enter a character: ")
if ch.isdigit():
    print(ch, "is a Digit")
elif ch.islower():
    print(ch, "is a Lowercase letter")
elif ch.isupper():
    print(ch, "is an Uppercase letter")
else:
    print(ch, "is a Special character")