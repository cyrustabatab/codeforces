


def puzzles():


    n,m = map(int,input().split())


    pieces = list(map(int,input().split()))

    pieces.sort()

    
    minimum = pieces[-1] - pieces[0]

    for i in range(0,len(pieces) - n + 1):
        diff = pieces[i + n -1 ] - pieces[i]
        minimum = min(minimum,diff)


    print(minimum)
        

puzzles()

