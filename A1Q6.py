from util import DistanceCalculator

class CalcDistance:
    print('Lets calculate the edit distance between two strings.')
    str1 = input('Input first string: ')
    str2 = input('Input second string: ')

    DC = DistanceCalculator()

    print('Edit distance between ', str1 , ' and ', str2, ': ', DC.distance(str1, str2))