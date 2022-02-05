from collections import defaultdict


def elephant():


    x = int(input())

    
    moves = defaultdict(int)
    moves[0] = 0
    

    steps = list(range(1,6))
    for i in range(1,x + 1):
        for step in steps:
            previous = i - step
            if moves.get(previous,None) is not None:
                moves[i] = min(moves.get(i,float("inf")),1 + moves[previous])


    
    print( moves[x])



elephant()





