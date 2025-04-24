import random
from words import words
import string
def get_valid_word(words):
    word = random.choice(words)  # randomly choose something from the list
    while '_' in word or '' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set () # what the user has gussed

    lives = 6


    # getting user input
    while len(word_letters) > 0 and lives > 0 :
        #letters used
        # " ".join (['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters:', ' '.join(used_letters))
        
        # what current word is (ie w - R D)

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
    
        # getting user input  
        user_letter = input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #take away a life if wrong
                print('Letter in not in word.')    
        elif user_letter in used_letters:
            print('You have already in used that character.Please try again.')
        else:
            print('Invalid character.Please try again.')
        # gets here when len (word_letters). == 0 OR when lives == 0
        if lives == 0:
            print('you died, sorry. The word was', word)
        else:
            print('you guessed the word', word, '!!')

hangman()