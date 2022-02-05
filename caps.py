


def caps():

    s = input()
    

    
    result = all(s[i].isupper() for i in range(1,len(s)))

    if result:
        s = s.swapcase()


    
    print(s)


caps()

