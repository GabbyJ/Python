import random

hangman_parts = [

"––––––"
"\n|    |"
"\n|    O"
"\n|"
"\n|"
"\n|"
"\n|"
"\n______",

"––––––"
"\n|    |"
"\n|    O"
"\n|    |"
"\n|    |"
"\n|"
"\n|"
"\n______",

"––––––"
"\n|    |"
"\n|    O"
"\n|   /|"
"\n|    |"
"\n|"
"\n|"
"\n______",

"––––––"
"\n|    |"
"\n|    O"
"\n|   /|\\"
"\n|    |"
"\n|"
"\n|"
"\n______",

"––––––"
"\n|    |"
"\n|    O"
"\n|   /|\\"
"\n|    |"
"\n|   /"
"\n|"
"\n______",

"––––––"
"\n|    |"
"\n|    O"
"\n|   /|\\"
"\n|    |"
"\n|   / \\"
"\n|"
"\n______",

" ______"
"\n| X  X |"
"\n| ____ |"
"\n|    U |"
"\n|______|",

" ______"
"\n| O  O |"
"\n|      |"
"\n| \\__/ |"
"\n|______|",

"––––––"
"\n|    |"
"\n|"
"\n|"
"\n|        O/"
"\n|       /|"
"\n|        |"
"\n______  / \\"



]


def hangman():
    secret_word = random.choice(["microsoft", "apple", "computer", "technology", "keyboard", "python", "javascript",
                                 "coding", "hamburger", "community", "representative", "milkshake", "dancing", "house",
                                 "twister", "yellow", "orange", "basketball", "football", "creativity", "mother",
                                 "family", "human", "president", "hilarious"])
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "~", "+", "=", "_", "[", "]", "{", "}", "|",
                          "/", "<", ">", "?", ",", ".", "`"]

    guess_count = 0
    guess_limit = 6
    guesses_left = 5
    guessed_letters = []
    wrong_letters = []

    print("\nWELCOME TO HANGMAN!")
    good_name = True
    while good_name:
        name = str(input("\nName your Hangman: ")).title()
        if name.isspace() or name.isdigit() or name == "" or name in special_characters or len(name) <= 1:
            print("Enter a valid name.")
        else:
            good_name = False
    print(hangman_parts[8])
    print("This is " + name + ". " + name + " doesn't want to hang. Don't kill " + name + ".")
    print("\nRules:\nFigure out the secret word before " + name + " hangs. You kill them, you lose."
          "\nIf you feel you know the word, just type it in at anytime! Good luck!")
    input("\nPress Enter to start playing... ")
    # print(secret_word)
    print("\nThe secret word has " + str(len(secret_word)) + " letters in it.")

    while guess_count < guess_limit:
        letters_in_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                letters_in_word = letters_in_word + letter
                if letters_in_word == secret_word:
                    print(hangman_parts[7])
                    print("You saved " + name + "!")
                    print("\nCongrats! You correctly guessed the word " + "'" + secret_word + "'.")
                    play()
                    break
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
                print("Already guessed " + "'" + guess + "'.")
            elif guess == secret_word:
                print(hangman_parts[7])
                print("You saved " + name + "!")
                print("\nCongrats! You correctly guessed the word " + "'" + secret_word + "'.")
                break
            elif guess in secret_word:
                print("'" + guess + "'" + " is in the word!")
                guessed_letters.append(guess)
            else:
                print(hangman_parts[guess_count])
                print("'" + guess + "'" + " is NOT in the word.\nYou have " + str(guesses_left) + " wrong guesses left.")
                guess_count += 1
                guesses_left -= 1
                wrong_letters.append(guess)
            print()

    while guess_limit == 6 and guess != secret_word:
        print(name + "'s about to die! Can you save them?")
        print("\nLast chance. Can you guess the word?")
        print(letters_in_word)
        final_guess = str(input("Enter the word: ")).lower()
        if final_guess == secret_word:
            print(hangman_parts[7])
            print("It's a miracle! You saved " + name + "!")
            print("\nCongrats! You correctly guessed the word " + "'" + secret_word + "'.")
            break
        elif len(final_guess) <= 2 or final_guess == "" or final_guess.isspace() or final_guess.isdigit() or final_guess in special_characters:
            print("\nEnter a valid word guess.")

        else:
            print(hangman_parts[6])
            print("Oh no, you killed " + name + "!")
            print("\nSorry. The word is " + "'" + secret_word + "'" + ". Better luck next time.")
            break


def play():
    play_again = True
    while play_again:
        keep_playing = input("\nPlay again? (y/n): ")
        affirmative = ['yes', 'yeah', 'yup', 'y', 'yea', 'si', 'sí', 'oui', 'ja', 'ha', 'hai', 'da']
        negative = ['n', 'no', 'naw', 'nah', 'nope', 'non', 'nein', 'nahi', 'net', 'lie']
        if keep_playing.lower() in affirmative:
            hangman()
        elif keep_playing.lower() in negative:
            play_again = False
            print("Thanks for playing!")
        else:
            print("\nYes or no.")
            play()
            break


def play_hangman():
    hangman()
    play()


play_hangman()
