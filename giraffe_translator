'''
Giraffe Language
vowels -> g
- - - - - - - - - - -
dog -> dgg
cat _. cgt
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print("Let's learn the Giraffe language!\nEvery vowel becomes a 'g'.\nTry it for yourself!")
print(translate(input("Enter a phrase: ")))
