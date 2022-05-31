from random import randrange


def generateList(start, end, number):

    if number > end - start:
        return "Error"

    R = list(range(start, end))

    l = []

    while number > 0:
        r = randrange(len(R))
        l.append(R[r])
        del R[r]
        number -= 1

    return l


class RandomGenerator:
    pass
