import random

def swap(input, seen=set()):
    new_word = input
    random_integer = random.randint(0, len(input)-2)

    if len(seen) == len(input):
        return input
    counter = 0
    while random_integer in seen and random_integer+1 in seen:
        if counter == 5:
            return (input, seen)
        random_integer = random.randint(0, len(input)-2)
        counter += 1
    seen.add(random_integer)
    seen.add(random_integer+1)

    a = new_word[random_integer]
    b = new_word[random_integer+1]

    new_word[random_integer+1] = a
    new_word[random_integer] = b

    return (new_word, seen)