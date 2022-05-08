import random


def getPlanet(answerNumber):
    if answerNumber == 1:
        return 'Sun'
    elif answerNumber == 2:
        return 'Mercury'
    elif answerNumber == 3:
        return 'Venus'
    elif answerNumber == 4:
        return 'Earth'
    elif answerNumber == 5:
        return 'Mars'
    elif answerNumber == 6:
        return 'Jupiter'
    elif answerNumber == 7:
        return 'Saturn'
    elif answerNumber == 8:
        return 'Uranus'

r = random.randint(1, 8)
planets = getPlanet(r)
print(f'Your planet is: {planets}')
print(getPlanet(random.randint(1, 8)))