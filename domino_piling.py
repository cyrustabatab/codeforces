


def domino_piling():


    rows,cols = map(int,input().split())

    
    #horizontal 

    
    values = ((rows,cols),(cols,rows))
    
    numbers = []
    for v1,v2 in values:
        dominos = v1//2 * v2

        if v1 % 2 == 1:
            dominos += v2//2

        numbers.append(dominos)



    dominos = max(numbers)
    print(dominos)



domino_piling()























