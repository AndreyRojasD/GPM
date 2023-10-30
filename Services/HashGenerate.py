import random

def hashing():
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(numbers)
    endhash = "".join(numbers)
    return endhash


