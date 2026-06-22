# Experiment 47: Substring Check Using Regular Expression

import re

string = input("Enter main string : ")
pattern = input("Enter substring/pattern: ")

if re.search(pattern, string):
    print(f'"{pattern}" found in "{string}"')
else:
    print(f'"{pattern}" NOT found in "{string}"')
