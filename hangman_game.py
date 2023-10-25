import random
import hangman_images
letter=["apple","banana","orange"]
#word=""
display=[]
life=0
word=random.choice(letter)
if word=="apple":
    print("HINT!! I'm a fruit, crisp and sweet,\n"
        "In pies and tarts, I'm quite a treat.\n"
        "I'm red or green, a healthy snack,\n"
        "A teacher's gift, a tree to track.\n"
        "What am I that you can find in a grove?\n" 
        "A word of five letters, can you solve? ")
if word=="banana":
    print("I'm a fruit with a peel so yellow,\n"
        "In bunches, I dangle, a cheerful fellow.\n"
        "I'm creamy inside, a tropical delight,\n"
        "In smoothies and splits, I'm just right.\n"
        "What am I that monkeys often adore?\n"
        "A word of six letters, can you explore?\n")
if word=="orange":
    print("I'm a citrus fruit, so round and bright\n,"
        "My color's like a sunset's light.\n"
        "When you're thirsty, I'm a juicy cure,\n"
        "With segments inside, so pure.\n"
        "What am I with a zesty tang to savor?\n"
        "A word of six letters, can you flavor?")

#print(word)
for i in range(len(word)):
    display+='_'
print(display)
flag=False
while not flag:
    guessed_char=str(input("Guess the char in the words : ").lower())
    for position in range(len(word)):
        new=word[position]
        if new==guessed_char:
            display[position]=guessed_char    
    print(display)
    if guessed_char not in word:
        life+=1;
        if life==6:
            flag=True
            print("game over")
    if '_' not in display:
            flag=True
            print("you win") 
    print(hangman_images.stages[life])

