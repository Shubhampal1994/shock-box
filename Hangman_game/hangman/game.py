from .exceptions import *
from random import randint

LIST_OF_WORDS = []

def _get_random_word(list_of_words):
    return (list_of_words[0] if len(list_of_words) == 1 else list_of_words[randint(0, len(list_of_words)-1)])
    
def _mask_word (word):
    return ('*' * len (word))

def _uncover_word (answer_word, masked_word, character):
    count = 0
    masked_word_list = []
    for asterisk in masked_word:
        masked_word_list.append (asterisk)
    for char in answer_word:
        if char == character:
            masked_word_list [count] = char
        count += 1
    return (''.join (masked_word_list))

def guess_letter (game, letter):
    if not game["masked_word"] or not game["answer_word"]:
        raise InvalidWordException()
    
    if len(letter) > 1:
        raise InvalidGuessedLetterException()
    
    for guesses in game["previous_guesses"]:
        if guesses == letter:
            raise InvalidGuessedLetterException ()
    
    updated_masked_word = _uncover_word (game ['answer_word'], game ['masked_word'], letter)
    if updated_masked_word == game['masked_word']:
        game['previous_guesses'].append(letter)
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = updated_masked_word
        game['previous_guesses'].append(letter)

def start_new_game (list_of_words = None, number_of_guesses = 5):
    word_to_guess = _get_random_word(list_of_words).lower()
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }
    return (game)