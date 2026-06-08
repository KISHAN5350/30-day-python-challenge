


# Experiment 31: Password Check Using While-Else

password = "python123"
attempts = 3

while attempts > 0:
    pwd = input("Enter password: ")
    
    if pwd == password:
        print("Access Granted!")
        break
    
    attempts -= 1
    print(f"Wrong password. {attempts} attempt(s) left.")
else:
    print("All attempts finished. Access Denied.")