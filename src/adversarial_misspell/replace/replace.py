import os
import re
from collections import defaultdict 
import random

chars = "~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/"

def replace(input, seen=set()):
    new_word = input
    random_integer = random.randint(0, len(input)-1)

    if len(seen) == len(input):
        return input
    while random_integer in seen:
        random_integer = random.randint(0, len(input)-1)
    seen.add(random_integer)

    new_word[random_integer] = chars[random.randint(0, len(chars)-1)]

    return (new_word, seen)