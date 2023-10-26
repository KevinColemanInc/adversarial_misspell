import os
import re
from collections import defaultdict 
import random

def duplicate(input, seen=set()):
    new_word = input
    random_integer = random.randint(0, len(input)-1)

    if len(seen) == len(input):
        return input
    while random_integer in seen:
        random_integer = random.randint(0, len(input)-1)
    seen.add(random_integer)

    num_dupes = random.randint(2, 4)

    org_character = input[random_integer]
    new_character = org_character * num_dupes
    new_word[random_integer] = new_character

    return (new_word, seen)