import json
import random
import string
f = open('words.json')
word_list = json.load(f)['data']

def get_valid_word():
    word = random.choice(word_list)
    while ' ' in word or '-' in word:
        word = random.choice(word_list)
    return word.lower()

def play():
    word = get_valid_word()
    letter_set = set(word)
    used_set = set()
    lives = 6
    while lives and len(letter_set):
        display = [letter if letter in used_set else '_' for letter in word]
        print('Lives:', lives)
        print('Word:', ' '.join(display))
        print('Used letters:', ' '.join([letter for letter in used_set]))
        choice = input('Enter a letter: ')
        choice = choice.lower()[0]
        if choice in used_set:
            print('You have already tried that letter, try something new!')            
        elif choice not in letter_set:
            print("That is not present in the word... you lost a life!")
            lives -= 1
        used_set.add(choice)
        letter_set.discard(choice)
        print()
        
    if len(letter_set):
        print(f'You died! The word was "{word}"')
    else:
        print(f'Congratulations! The word was "{word}"')

play()

