# Add more congrats/failed options- Grades (if/else)  √
# Update/add questions (strings) √
# Turn scores into percentages (math) √
# Allow multiple versions of the answer √
# Make more interactive
    # Obvious place to put answer (update input)√
    # Add right/wrong to each question (if/else)
# Make either easy, medium, hard levels OR Pick 1 of 3 topics (2nd class or if/else, while)
# Play again option (while)
    # Yes = shows answers(?), start again
    # No = show answers


class Question:
    def __init__(self, prompt):
        self.prompt = prompt


question_prompts = [
    "What movie used the song 'My Heart Will Go On'?\n(a) Avatar\n(b) Overboard\n(c) Titanic\n\n",
    "\nWho sings 'Livin on a Prayer'?\n(a) Bon Jovi\n(b) AC/DC\n(c) Bruce Springsteen\n\n",
    "\nWhat band did a remake of 'Africa' by Toto?\n(a) Maroon 5\n(b) Weezer\n(c) Linkin Park\n\n",
    "\nWho wrote and performed the hit song 'Uptown Funk'?\n(a) Nick Jonas\n(b) Bruno Mars\n(c) Justin Timberlake\n\n",
    "\nWhat is Lady Gaga's fan base called?\n(a) Little Monsters\n(b) Beyhive\n(c) Swifties\n\n",
    "\nWho was the first rapper to win a grammy?\n(a) Tupac\n(b) Jay Z\n(c) Will Smith\n\n",
    "\nWhat artist originally sang 'I Will Always Love You'?\n(a) Whitney Houston\n(b) Dolly Parton\n(c) Kenny Rogers\n\n",
    "\nWho is the most recent EGOT winner?\n(a) John Legend\n(b) Beyonce\n(c) Adele\n\n",
    "\nWhich movie musical is about Barnum & Baily Circus?\n(a) A Star is Born\n(b) La La Land\n(c) The Greatest Showman\n\n",
    "\nWho performed 'Piano Man'?\n(a) Paul McCartney\n(b) Billy Joel\n(c) Elton John\n\n"
]

questions = [
    Question(question_prompts[0]),
    Question(question_prompts[1]),
    Question(question_prompts[2]),
    Question(question_prompts[3]),
    Question(question_prompts[4]),
    Question(question_prompts[5]),
    Question(question_prompts[6]),
    Question(question_prompts[7]),
    Question(question_prompts[8]),
    Question(question_prompts[9])
]

answer_options =[
    ["c", "titanic"],
    ["a", "bon jovi"],
    ["b", "weezer"],
    ["b", "bruno mars"],
    ["a", "little monsters"],
    ["c", "will smith"],
    ["b", "dolly parton"],
    ["a", "john legend"],
    ["c", "the greatest showman", "greatest showman"],
    ["b", "billy joel"]
]

import math


def run_test(questions):
    score = 0
    count = 0
    for question in questions:
        print(question.prompt)
        answer = input("Your answer: ").lower()
        if answer in answer_options[count]:
            score += 1
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
            print("\nYou got an E. " + str(scores) + "%" + "\nEhh... you kind of suck at this. You should learn more random music facts.")
        else:
            print("\nF?! How? " + str(scores) + "%" + "\nDo you just hate music?!")

    scores = float((score * 100) / len(questions))
    scores = math.floor(float(scores))
    determine_grade(scores)


print("\nMUSIC TRIVIA GAME\nTest your musical knowledge.\n")
run_test(questions)
