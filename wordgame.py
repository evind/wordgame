"""
@author: Evin Darling C00144257
@course: Software Development Year 3
@lecturer: Paul Barry
@description: A word guessing game. Web and Cloud dev assignment 1
"""


import time
import pickle
import functions


functions.print_rules()
user_prompt = input('Ready to play? (y/n): ')

while user_prompt == 'y':
    rules = {'valid_input': True, 'invalid_letters': [],
             'invalid_words': [], 'small_words': [],
             'duplicate_words': [], 'source_word_check': False}
    prev_words = []

    try:
        leaderboard = pickle.load(open('data/leaderboard.p', 'rb'))
    except FileNotFoundError:
        leaderboard = {}
        pickle.dump(leaderboard, open('data/leaderboard.p', 'wb'))

    dictionary = functions.create_dictionary()
    source_word = functions.pick_source_word(dictionary).lower()

    print('\nYour word is:', source_word)
    print('\nEnter 7 (space separated) words: ')

    curr_time = time.time()
    user_input = input('> ')
    user_input = user_input.lower()
    end_time = time.time()
    total_time = round(end_time - curr_time, 4)
    user_input_list = user_input.split()

    if len(user_input_list) != 7:
        print('Invalid number of words:', len(user_input_list), '/ 7')
        rules['valid_input'] = False

    for word in user_input_list:
        temp_list = list(source_word)
        # 1. check if word made from letters in source
        for ch in word:
            if ch in temp_list:
                temp_list.remove(ch)
            else:
                if ch not in rules['invalid_letters']:
                    rules['invalid_letters'].append(ch)
                rules['valid_input'] = False
        # 2. check if word exists in dictionary
        if word not in dictionary:
            rules['invalid_words'].append(word)
            rules['valid_input'] = False
        # 3. check if word is 3+ letters
        if len(word) < 3:
            rules['small_words'].append(word)
            rules['valid_input'] = False
        # 4. check if word is duplicate
        if word in prev_words:
            rules['duplicate_words'].append(word)
            rules['valid_input'] = False
        prev_words.append(word)
        # 5. check if word is source word
        if word == source_word:
            rules['source_word_check'] = True
            rules['valid_input'] = False

    if rules['valid_input']:
        print('\nWinner Winner Chicken Dinner!\n')
        print('Your time: ', total_time)
        name = input('Enter your name: ')

        leaderboard[total_time] = name
        pickle.dump(leaderboard, open('data/leaderboard.p', 'wb'))
        functions.print_top_ten(leaderboard)
        position = functions.find_position(leaderboard, name, total_time)

        if position <= 10:
            print('\nCongrats! You made the top ten!\n')
            print('You placed:', position)
        else:
            print('\nYou placed: #', position)
    else:
        functions.print_errors(rules)
        print('\nEveryone is a winner! (except you (you lost))')
    user_prompt = input('Would you like to play again? (y/n) ')
