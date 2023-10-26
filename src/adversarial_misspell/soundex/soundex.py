import os
from utils import load, get, dump, exists
import re
from collections import defaultdict 
import random

def soundex(input, seen=set()):
    new_word = input
    random_integer = random.randint(0, len(input)-1)

    if len(seen) == len(input):
        return input
    while random_integer in seen:
        random_integer = random.randint(0, len(input)-1)
    seen.add(random_integer)

    org_character = input[random_integer]
    
    new_character = _preprocess(org_character)
    if new_character == '':
        new_word[random_integer] = new_character

    return (new_word, seen)

# write the soundex algorithm in python for a list of characters
def soundex(characters):
    soundex_dict = {
        'A': '0', 'E': '0', 'I': '0', 'O': '0', 'U': '0', 'Y': '0',
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }

    def get_soundex_code(character):
        character = character.upper()
        if character in soundex_dict:
            return soundex_dict[character]
        return ''

    soundex_code = ''
    for character in characters:
        code = get_soundex_code(character)
        if code != '':
            if soundex_code == '':
                soundex_code += code
            elif code != soundex_code[-1]:
                soundex_code += code

    return soundex_code

def _preprocess(char):
    # if non-ascii drop all non-ascii
    if ord(char) < 128:
        return char
    return ''
