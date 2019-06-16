import random


def hangman():
    secret_word = random.choice(["microsoft", "apple", "linux", "computer", "ubuntu", "technology", "keyboard"])
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "~", "+", "=", "_", "[", "]", "{", "}", "|",
                          "/", "<", ">", "?", ",", ".", "`"]
    guess_count = 0
    guess_limit = 6
    guesses_left = 5
    guessed_letters = []
    wrong_letters = []

    print("Welcome to Hangman!\nRules: You kill him, you lose. Good luck!\n")
    print(secret_word)
    print("This word has " + str(len(secret_word)) + " letters in it.")

    while guess_count < guess_limit:
        letters_in_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                letters_in_word = letters_in_word + letter
            else:
                letters_in_word = letters_in_word + "_"

        print("Word: " + letters_in_word)
        guess = str(input("Enter a letter: ")).lower()

        if guess == "" or guess.isspace() or guess.isdigit() or guess in special_characters:
            print("\nPlease enter a letter.")
        elif len(guess) > 1 and guess != secret_word:
            print("\nOnly guess multiple letters if you know the word... right now you don't.")
        else:
            if guess in guessed_letters or guess in wrong_letters:
                print("Already guessed " + "'" + guess + "'")
            elif guess == secret_word:
                print("Congrats! You correctly guessed the word " + "'" + secret_word + "'")
                break
            elif guess in secret_word:
                print("'" + guess + "'" + " is in the word!")
                guessed_letters.append(guess)
            else:
                print("'" + guess + "'" + " is NOT in the word.\n You have " + str(guesses_left) + " wrong guesses left.")
                guess_count += 1
                guesses_left -= 1
                wrong_letters.append(guess)
            print()

    while guess_limit == 6 and guess != secret_word:
        print("Last chance. Can you guess the word?")
        print(letters_in_word)
        final_guess = input("Enter the word: ")
        if final_guess == secret_word:
            print("Congrats! You correctly guessed the word " + "'" + secret_word + "'")
            break
        elif len(final_guess) <= 2 or final_guess == "" or final_guess.isspace() or final_guess.isdigit() or final_guess in special_characters:
            print("\nEnter a valid word guess.")

        else:
            print("Sorry. The word is " + "'" + secret_word + "'" + ". Better luck next time.")
            break


def play():
    play_again = True
    while play_again:
        keep_playing = input("Play again? (y/n): ")
        affirmative = ['yes', 'yeah', 'yup', 'y', 'yea', 'si', 'sí', 'oui', 'ja', 'ha', 'hai', 'da']
        negative = ['n', 'no', 'naw', 'nah', 'nope', 'non', 'nein', 'nahi', 'net', 'lie']
        if keep_playing.lower() in affirmative:
            hangman()
        elif keep_playing.lower() in negative:
            play_again = False
            print("Thanks for playing!")
        else:
            print("Yes or no.")
            play()
            break


def play_hangman():
    hangman()
    play()


play_hangman()
