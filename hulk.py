


def hulk():

    
    n = int(input())

    string = []
    for i in range(1,n + 1):
        if i % 2 == 0:
            s = "I love"
        else:
            s =  "I hate"

        if i == n:
            s += ' it'
        else:
            s += ' that'

        string.append(s)


    

    print(' '.join(string))


hulk()
