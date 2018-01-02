from hangman.game import start_new_game, guess_letter
from hangman.exceptions import *

LIST_OF_WORDS = ['water', 'carbon', 'oxygen']

def build_list_of_words(words, default_list):
    if words:
        words_list = words.split(',')
        count = 0
        for words_lists_word in words_list:
            new_word = words_lists_word.strip(' ')
            words_list[count] = new_word
            count += 1
        return (words_list)
    return (default_list)

def main():
    print('*******************')
    print('##### HANGMAN #####')
    print('*******************')

    try:
        words = input('Enter your list of words separated by comma. Leave empty for default: ')
        if words == " ":
            raise InvalidListOfWordsException()
    except InvalidListOfWordsException:
        print("You have entered an Invalid list!")
        print("Restarting Game...")
        print()
        main()

    list_of_words = build_list_of_words(words, LIST_OF_WORDS)
    attempts = input('Enter how many number of attempts allowed. Leave empty for default: ')
    
    if attempts:
        game = start_new_game(list_of_words, int(attempts))
    else:
        game = start_new_game(list_of_words)
    print('\n### Game Initialized. Let\'s play!! ###\n')

    try:
        while True:
            print()
            if game["remaining_misses"] == 0:
                raise GameLostException()
            previous_masked_word = game['masked_word']
            line_message = '({}) Enter new guess ({} remaining attempts): '.format(
                previous_masked_word, game['remaining_misses'])
            
            users_guess = input(line_message).lower()
            try:
                guess_letter(game, users_guess)
            except InvalidGuessedLetterException:
                print('\t Your guess is incorrect. Please guess again.')
                continue

            new_masked_word = game['masked_word']

            if new_masked_word != previous_masked_word:
                print('\tCongratulations! That\'s correct.')
            else:
                print('\t:( That\'s a miss!')
            
            if new_masked_word == game["answer_word"]:
                raise GameWonException

    except GameWonException:
        print('\t YES! You win! The word was: {}'.format(game['answer_word']))

    except GameLostException:
        print('\t :( OH NO! You Lose! The word was: {}'.format(game['answer_word']))
    
    except InvalidWordException:
        print("The word was Invalid!")
        print("Restarting Game...")
        print()
        main()

if __name__=='__main__':
    main()