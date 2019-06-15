# Add more congrats/failed options- Grades (if/else)  √
# Update/add questions (strings) √
# Turn scores into percentages (math) √
# Allow multiple versions of the answer √
# Make more interactive √
    # Obvious place to put answer (update input) √
    # Add right/wrong to each question (if/else) √
# Make either easy, medium, hard levels OR Pick 1 of 3 topics (2nd class or if/else, while) √
# Play again option (while) √

import math


class Question:
    def __init__(self, prompt):
        self.prompt = prompt


question_prompts = [
    [
        "1. What movie used the song 'My Heart Will Go On'?\n(a) Avatar\n(b) Overboard\n(c) Titanic\n\n",
        "\n2. Who sings 'Livin on a Prayer'?\n(a) Bon Jovi\n(b) AC/DC\n(c) Bruce Springsteen\n\n",
        "\n3. Who wrote and performed the hit song 'Uptown Funk'?\n(a) Nick Jonas\n(b) Bruno Mars\n(c) Justin Timberlake\n\n",
        "\n4. What was Beethoven's first name?\n(a) Ludwig\n(b) Wolfgang\n(c) Johann\n\n",
        "\n5. What is Lady Gaga's fan base called?\n(a) Little Monsters\n(b) Beyhive\n(c) Swifties\n\n",
        "\n6. Which movie musical is about Barnum & Baily Circus?\n(a) A Star is Born\n(b) La La Land\n(c) The Greatest Showman\n\n",
        "\n7. Who performed 'Piano Man'?\n(a) Paul McCartney\n(b) Billy Joel\n(c) Elton John\n\n",
        "\n8. What band was Michael Jackson in?\n(a) Jackson 5\n(b) Temptations\n(c) Mike & Brothers\n\n",
        "\n9. 'Pure Imagination' is a song from which children's film?\n(a) Lion King\n(b) Willy Wonka & the Chocolate Factory\n(c) James & the Giant Peach\n\n",
        "\n10. Who has won lots of awards for her pop song 'Hello'?\n(a) Adele\n(b) Beyonce\n(c) Ariana Grande\n\n"
    ],
    [
        "1. What band did a remake of 'Africa' by Toto?\n(a) Maroon 5\n(b) Weezer\n(c) Linkin Park\n\n",
        "\n2. What city was Motown invented\n(a) Detroit\n(b) Philadelphia\n(c) Chicago\n\n",
        "\n3. Who was the first rapper to win a grammy?\n(a) Tupac\n(b) Jay Z\n(c) Will Smith\n\n",
        "\n4. What is the better known stage name of Robyn Fenty?\n(a) Rihanna\n(b) P!nk\n(c) Mariah Carey\n\n",
        "\n5. What artist originally sang 'I Will Always Love You'?\n(a) Whitney Houston\n(b) Dolly Parton\n(c) Kenny Rogers\n\n",
        "\n6. Who is the most recent EGOT winner?\n(a) John Legend\n(b) Beyonce\n(c) Adele\n\n",
        "\n7. Who sang 'I Want to Hold Your Hand'?\n(a) The Supremes\n(b) Bruce Springsteen\n(c) The Beatles\n\n",
        "\n8. Sean John Combs is better known by what stage name?\n(a) Puff Daddy\n(b) Jay Z\n(c) Sean Paul\n\n",
        "\n9. American Idiot is a rock musical based on what band's album?\n(a) My Chemical Romance\n(b) Green Day\n(c) Nirvana\n\n",
        "\n10. What song holds the record for the most watched Youtube video\n(a) Uptown Funk\n(b) Despacito\n(c) Gangnam Style\n\n"
    ],
    [
        "1. Dolly Parton had a 1981 hit with which song from the film of the same name?\n(a) Reba McEntire\n(b) Dolly Parton\n(c) Martina McBride\n\n",
        "\n2. The Copacabana nightclub was in which city?\n(a) Detroit\n(b) Los Angeles\n(c) New York\n\n",
        "\n3. Which artist made a song titled 'Ashes' specifically for the movie Deadpool 2?\n(a) Celine Dion\n(b) Kelly Clarkson\n(c) Ryan Reynolds\n\n",
        "\n4. What band was Phil Collins in before he went solo?\n(a) Genesis\n(b) Exodus\n(c) Leviticus\n\n",
        "\n5. Whose nickname was a derived from the term satchel-mouth?\n(a) Miles Davis\n(b) Louis Armstrong\n(c) Sammy Davis Jr.\n\n",
        "\n6. Who originally sang 'Hound Dog'?\n(a) Ray Charles\n(b) Elvis Presley\n(c) Big Mama Thornton\n\n",
        "\n7. Lynyrd Skynyrd had a massive hit with which song that was also the title of a film starring Reese Witherspoon?\n(a) Sweet Home Alabama\n(b) Free Bird\n(c) Saturday Night Special\n\n",
        "\n8. Which rap stars collaborated on the 2011 album 'Watch the Throne'?\n(a) Jay Z and Eminem\n(b) Eminem and Kanye West\n(c) Jay Z and Kanye West\n\n",
        "\n9. Who played 27 different instrument son their debut album 'For You'?\n(a) Stevie Wonder\n(b) Prince\n(c) Curtis Mayfield\n\n",
        "\n10. Which movie is 'Can't Stop the Feeling' by Justin Timberlake from?\n(a) Pitch Perfect 2\n(b) Trolls\n(c) Zootopia\n\n"
    ]
]

questions = [
    [
        Question(question_prompts[0][0]),
        Question(question_prompts[0][1]),
        Question(question_prompts[0][2]),
        Question(question_prompts[0][3]),
        Question(question_prompts[0][4]),
        Question(question_prompts[0][5]),
        Question(question_prompts[0][6]),
        Question(question_prompts[0][7]),
        Question(question_prompts[0][8]),
        Question(question_prompts[0][9])
    ],
    [
        Question(question_prompts[1][0]),
        Question(question_prompts[1][1]),
        Question(question_prompts[1][2]),
        Question(question_prompts[1][3]),
        Question(question_prompts[1][4]),
        Question(question_prompts[1][5]),
        Question(question_prompts[1][6]),
        Question(question_prompts[1][7]),
        Question(question_prompts[1][8]),
        Question(question_prompts[1][9])
    ],
    [
        Question(question_prompts[2][0]),
        Question(question_prompts[2][1]),
        Question(question_prompts[2][2]),
        Question(question_prompts[2][3]),
        Question(question_prompts[2][4]),
        Question(question_prompts[2][5]),
        Question(question_prompts[2][6]),
        Question(question_prompts[2][7]),
        Question(question_prompts[2][8]),
        Question(question_prompts[2][9])
    ],
]

answer_options = [
    [
        ["c", "titanic"],
        ["a", "bon jovi"],
        ["b", "bruno mars"],
        ["a", "ludwig"],
        ["a", "little monsters"],
        ["c", "the greatest showman", "greatest showman"],
        ["b", "billy joel"],
        ["a", "jackson 5", "jackson five"],
        ["b", "willy wonka & the chocolate factory", "willy wonka and the chocolate factory", "willy wonka"],
        ["a", "adele"]
    ],
    [
        ["b", "weezer"],
        ["a", "detroit"],
        ["c", "will smith"],
        ["a", "rihanna"],
        ["b", "dolly parton"],
        ["a", "john legend"],
        ["c", "beatles", "the beatles", "beetles"],
        ["a", "puff daddy", "diddy", "p. diddy", "p diddy"],
        ["b", "green day"],
        ["b", "despacito", "despasito"]
    ],
    [
        ["b", "dolly parton", "dolly"],
        ["c", "new york", "newyork", "ny"],
        ["a", "celine dion", "celine"],
        ["a", "genesis"],
        ["b", "louis armstrong", "louis"],
        ["c", "big mama thornton", "big mama", "thornton"],
        ["a", "sweet home alabama"],
        ["c", "jay z and kanye west", "jay z kanye west", "jay z and kanye", "jay z kanye", "jay and kanye"],
        ["b", "prince"],
        ["b", "trolls"]
    ]
]

picked_level = 0


def levels():
    difficulty = True
    while difficulty:
        global picked_level
        level = input("Pick a level (1, 2, 3): ")
        if level == '1':
            picked_level = 0
            difficulty = False
            print("\nYou picked easy, so don't fail.\n")
            run_test(questions[0])
        elif level == '2':
            picked_level = 1
            difficulty = False
            print("\nYou picked medium. Enjoy!\n")
            run_test(questions[1])
        elif level == '3':
            picked_level = 2
            difficulty = False
            print("\nYou picked hard... good luck!\n")
            run_test(questions[2])
        else:
            difficulty = True
            print("What? I said 1, 2, or 3. Stop being hard headed!")


def run_test(questions):
    score = 0
    count = 0

    for question in questions:
        print(question.prompt)
        answer = input("Your answer: ").lower()
        picked = True
        while picked:
            if answer in answer_options[picked_level][count]:
                picked = False
                score += 1
                print("Correct!")
            elif answer == "" or answer.isspace() or answer.isdigit():
                answer = input("Please provide an answer: ")
            else:
                picked = False
                print("Wrong. The answer was " + str(answer_options[picked_level][count][1]).title())
        count += 1

    def determine_grade(scores):
        if scores >= 90 and scores <= 100:
            print("\nYou got an A! " + str(scores) + "%" + "\nGreat job!")
        elif scores >= 80 and scores <= 89:
            print("\nYou got a B! " + str(scores) + "%" + "\nGood job!")
        elif scores >= 70 and scores <= 79:
            print("\nYou got a C. " + str(scores) + "%" + "\nC's get degrees too...")
        elif scores >= 60 and scores <= 69:
            print("\nYou got a D. " + str(scores) + "%" + "\nBetter luck next time!")
        elif scores >= 50 and scores <= 59:
            print("\nYou got an E. " + str(
                scores) + "%" + "\nEhh... you kind of suck at this. You should learn more random music facts.")
        else:
            print("\nF?! How? " + str(scores) + "%" + "\nDo you just hate music?!")

    scores = float((score * 100) / len(questions))
    scores = math.floor(float(scores))
    determine_grade(scores)


def playing_still():
    keep_playing = True
    while keep_playing:
        play_again = input("\nPlay again? (y/n): ")
        affirmative = ['yes', 'yeah', 'yup', 'y', 'yea', 'si', 'sí', 'oui', 'ja', 'ha', 'hai', 'da']
        negative = ['n', 'no', 'naw', 'nah', 'nope', 'non', 'nein', 'nahi', 'net', 'lie']
        if play_again.lower() in affirmative:
            main()
            break
        elif play_again.lower() in negative:
            keep_playing = False
            print("Thanks for playing!")
        else:
            print("YES. Or NO. Listen!")
            playing_still()
            break


def main():
    levels()
    playing_still()


main()
