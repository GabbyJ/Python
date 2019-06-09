# Add more congrats/failed options- Grades (if/else)
# Update/add questions (strings) √
# Turn scores into percentages (math) √
# Make more interactive
    # Obvious place to put answer (update input)√
    # Add right/wrong to each question (if/else)


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What movie used the song 'My Heart Will Go On'?\n(a) Avatar\n(b) Overboard\n(c) Titanic\n\n",
    "\nWho sings 'Livin on a Prayer'?\n(a) Bon Jovi\n(b) AC/DC\n(c) Bruce Springsteen\n\n",
    "\nWhat band did a remake of 'Africa' by Toto?\n(a) Maroon 5\n(b) Weezer\n(c) Linkin Park\n\n",
    "\nWho wrote and performed the hit song 'Uptown Funk'?\n(a) Nick Jonas\n(b) Bruno Mars\n(c) Justin Timberlake\n\n",
    "\nWhat is Lady Gaga's fan base called?\n(a) Little Monsters\n(b) Beyhive\n(c) Swifties\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        answer = input("Your answer: ")
        if answer == question.answer:
            score += 1
    print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct")
    print("Your percentage is " + str((score*100)/len(questions)) + "%")

print("\nMUSIC TRIVIA GAME\nTest your musical knowledge.\n")
run_test(questions)
