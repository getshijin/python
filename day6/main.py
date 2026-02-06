import random

word =["Camel","rock","man"]

random_word = random.choice(word)
print(random_word)
len_word = len(random_word)

display=""
for i in range(len_word):
    display += "_"

print(display)
guess_letter = input("Guess the letter")
print(guess_letter)

#a
if guess_letter in random_word:
    for letter in range(len(random_word)):
        #print(letter)
        if guess_letter == letter:
            display +=guess_letter
        else:
            display+="_"
    print(display)
else:
    print(display)
