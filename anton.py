from collections import Counter


def games():

    n = int(input())


    s = input()

    counts = Counter(s)

    
    count_a = counts['A']
    count_d = counts['D']


    if count_a > count_d:
        print('Anton')
    elif count_d > count_a:
        print('Danik')
    else:
        print('Friendship')


games()


