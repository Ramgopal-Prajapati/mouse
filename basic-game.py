import tkinter as tk
from random import randint

# Create the main window
root = tk.Tk()
root.title("Guess the Number Game")

# Generate a random number
random_number = randint(1, 10)

def check_guess():
    # Get the value from the entry box
    user_guess = int(entry.get())

    # Determine if the guess is too high, too low, or just right
    if user_guess > random_number:
        msg = "Too high!"
    elif user_guess < random_number:
        msg = "Too low!"
    else:
        msg = "Correct!"

    # Show the result
    result_label.config(text=msg)

# Create widgets
entry = tk.Entry(root)
entry.pack(padx=20, pady=20)

result_label = tk.Label(root)
result_label.pack(padx=20, pady=20)

check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack(padx=20, pady=20)

# Start the main loop
root.mainloop()
