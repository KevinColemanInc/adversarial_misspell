import os
from utils import load, get, dump, exists
import re
from collections import defaultdict 
import random

confusables = None
cache_path = 'static/homoglyph_confusables.json'

def homoglyph(input, seen=set()):
    if not exists(cache_path):
        raise Exception("Missing static/homoglyph_confusables.json. please run refresh()")

    confusables = None
    if confusables is None:
        confusables = load(cache_path)

    new_word = input
    random_integer = random.randint(0, len(input)-1)

    if len(seen) == len(input):
        return input
    while random_integer in seen:
        random_integer = random.randint(0, len(input)-1)
    seen.add(random_integer)

    org_character = input[random_integer]
    new_character = random.choice(confusables[org_character])["c"]
    new_word[random_integer] = new_character
    return (new_word, seen)

def refresh():
    """Refreshes Unicode confusables specification from ftp://ftp.unicode.org/Public/security/latest/confusables.txt"""
    return _generate_confusables_cache()

def _generate_confusables_cache():
    """Saves Unicode confusables specification as json file

    :return: True for success, raises otherwise.
    :rtype: bool
    """
    url = 'ftp://ftp.unicode.org/Public/security/latest/confusables.txt'
    file = get(url)
    confusables_matrix = defaultdict(list)
    match = re.compile(r'[0-9A-F ]+\s+;\s*[0-9A-F ]+\s+;\s*\w+\s*#'
                       r'\*?\s*\( (.+) → (.+) \) (.+) → (.+)\t#',
                       re.UNICODE)
    for line in file:
        p = re.findall(match, line)
        if p:
            char1, char2, name1, name2 = p[0]
            confusables_matrix[char1].append({
                'c': char2,
                'n': name2,
            })
            confusables_matrix[char2].append({
                'c': char1,
                'n': name1,
            })

    dump(cache_path, dict(confusables_matrix))