


def ultra_fast():

    s1 = input()
    s2 = input()


    result = []


    for c1,c2 in zip(s1,s2):
        result.append('1' if c1 != c2 else '0')


    print(''.join(result))


ultra_fast()


