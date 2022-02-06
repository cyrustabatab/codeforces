


def polys():
    

    mapping = {'I': 20,'C': 6,'O': 8,'T': 4,'D': 12}
    n = int(input())

    s = 0
    for _ in range(n):
        figure = input()
        s += mapping[figure[0]]

    
    print(s)


polys()



