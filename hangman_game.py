import random
import hangman_images
letter=["apple","banana","orange"]
#word=""
display=[]
life=0
word=random.choice(letter)
print(word)
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

