while True:
    user_input = input("Enter a number (or type 'Quit' to exit): ")
    num = float(user_input)

    if user_input.lower() == "quit":
        print("Program ended.")
        break

    
    

    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")