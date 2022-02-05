


def petya_and_strings():

    s1 = input()
    s2 = input()

    

    
    for c1,c2 in zip(s1,s2):
        c1 = c1.lower()
        c2 = c2.lower()
        if c1 < c2: 
            print(-1)
            break
        elif c1 > c2:
            print(1)
            break
    else:
        print(0)





petya_and_strings()
