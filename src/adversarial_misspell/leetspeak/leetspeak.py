import os
from utils import load, get, dump, exists
import re
from collections import defaultdict 
import random

leetspeak_dict = {
                'a': ['4', '@', 'A', 'a', '/\\', '/-\\'],
                'b': ['8', 'B', '|3', 'b', '13', '!3', '6', 'I3', '!3', '/3'],
                'c': ['(', '[', '{', '<', 'C', 'c'],
                'd': ['|)', '|]', 'D', 'd', 'cl', 'cI', 'I)', 'I]'],
                'e': ['3', 'E', 'e', '[-'],
                'f': ['|=', 'F', 'f', '/=', 'I=', 'ph'],
                'g': ['6', '9', 'G', 'g', '(_-', '(_+', 'C-', '[,'],
                'h': ['#', '|-|', 'H', 'h', '|~|', 'I-I', 'I~I', ']-[', ']~[', '}{', ')-(', '(-)', ')~(', '(~)'],
                'i': ['1', '!', '|', 'I', 'i', '[]'],
                'j': ['_|', 'J', 'j'],
                'k': ['|<', 'K', 'k', '|c', 'Ic', '|{', '|('],
                'l': ['1', '|_', 'L', 'l', '|', '7'],
                'm': ['|\\/|', 'M', 'm'],
                'n': ['|\\|', 'N', 'n'],
                'o': ['0', 'O', 'o'],
                'p': ['|D', '|o', 'P', 'p'],
                'q': ['(,)', 'Q', 'q'],
                'r': ['|2', 'R', 'r'],
                's': ['5', '$', 'S', 's'],
                't': ['7', '+', 'T', 't', '-|-', '~|~'],
                'u': ['|_|', 'U', 'u', '(_)', 'L|'],
                'v': ['\\/', 'V', 'v'],
                'w': ['\\/\\/', 'VV', '\\N', '\'//', '\\\'', '\\^/', '(n)', '\\V/', '\\X/', '\\|/', '\\_|_/', '\\_:_/', 'uu', '2u', '\\\\//\\\\//', 'w', 'W'],
                'x': ['%', '><', 'X', 'x'],
	        'y': ['j', '`/', '7', '\\|/', '\\//', 'Y', 'y'],
                'z': ['2', '7_', '-/_', '%', '>', 's', '~/_', '-\\_', '-|_', 'z', 'Z'],
                ' ': ['-', '_', ' '],
    }

def leetspeak(input, seen=set()):
    new_word = input
    random_integer = random.randint(0, len(input)-1)

    if len(seen) == len(input):
        return input
    while random_integer in seen:
        random_integer = random.randint(0, len(input)-1)
    seen.add(random_integer)

    org_character = input[random_integer]
    new_character = random.choice(leetspeak_dict[org_character])
    new_word[random_integer] = new_character
    return (new_word, seen)