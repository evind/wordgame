"""
@author: Evin Darling C00144257
@course: Software Development Year 3
@lecturer: Paul Barry
@description: Functions for wordgame.py
"""


import random


def create_dictionary():
    with open('data/words.txt', errors='ignore') as df:
        rawdata = df.read()
    dictionary = rawdata.split()
    return dictionary


def pick_source_word(dictionary):
    source_word_list = []
    for word in dictionary:
        if len(word) >= 7:
            source_word_list.append(word)
    random_int = random.randint(0, len(source_word_list) - 1)
    return source_word_list[random_int]


def print_errors(rules):
    if rules['invalid_letters']:
        print('Invalid letters: ', end='')
        print_list(rules['invalid_letters'])
    if rules['invalid_words']:
        print('Invalid words: ', end='')
        print_list(rules['invalid_words'])
    if rules['small_words']:
        print('Small words: ', end='')
        print_list(rules['small_words'])
    if rules['duplicate_words']:
        print('Duplicate words: ', end='')
        print_list(rules['duplicate_words'])
    if rules['source_word_check']:
        print('You may not use the source word!')


def print_rules():
    print('Hello, this is Word Game')
    print('------------------------')
    print('A word of seven or more characters will appear on screen, and',
          'the timer will start.')
    print('Your objective is to come up with seven words made of letters',
          'from the source word.')
    print('')
    print('Rules -- Each word must:')
    print('------------------------')
    print('1. Be made of letters from the source word. No reusing letters.')
    print('2. Exist in the dictionary.')
    print('3. Have 3 or more letters.')
    print('4. Not be a duplicate of a previous word.')
    print('5. Not be the source word itself.')


def print_list(lst):
    for element in lst[:-1]:
        print(element, end=', ')
    print(lst[-1], end='.\n')


def print_top_ten(leaderboard):
    count = 1
    print('\nTop Scorer List')
    print('===============================', end='')
    print('\n#)', 'Name', '\tTime', sep='\t')
    print('===============================')
    for k, v in sorted(leaderboard.items()):
        print(count, ')', '\t', v, '\t\t', k, sep='')
        count += 1
        if count == 11:
            break


def find_position(leaderboard, name, total_time):
    count = 1
    for k, v in sorted(leaderboard.items()):
        if k == total_time and v == name:
            return count
        else:
            count += 1
    return -1
