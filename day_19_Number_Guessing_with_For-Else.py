# Experiment 32: Number Guessing with For-Else

secret = 42

for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}: Guess the number: "))
    
    if guess == secret:
        print("Correct! You guessed it!")
        break
else:
    print("Better luck next time! The number was", secret)
