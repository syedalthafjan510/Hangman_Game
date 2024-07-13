import random
import hangman_stages
import words
print("  WELCOME TO HANGMAN GAME..........🤪🤪🧑🏻‍🦱🤪🤪🤪")
print(" you have 6 LIVES , so guess a correct word to win")
lives = 6
chosen_word = random.choice(words.words)
#print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter : ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("YOU LOSE.....!😞😞😞😞")
    if '_' not in display:
        game_over = True
        print("YOU WIN..........!🥳🥳🥳")
    print(hangman_stages.stages[lives])
print(f" The Word is {chosen_word}")