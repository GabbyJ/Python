secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("Guess the Word!\nYou get 3 guesses. Good luck!\n")
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("\nOut of guesses, YOU LOSE!\nThe word was \"giraffe\"")
else:
    print("\nCongrats! You win!")
input('\nPress Enter to leave the program')
