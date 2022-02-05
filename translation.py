



def translation():

    s1 = input()
    s2 = input()


    if len(s1) != len(s2):
        print('NO')
    else:
        for c1,c2 in zip(s1,reversed(s2)):
            if c1 != c2:
                print('NO')
                break
        else:
            print('YES')



translation()
