import math


def theater_square():


    n,m,a = map(int,input().split())


    

    rows = math.ceil(n /a)
    cols = math.ceil(m / a)



    number = rows * cols

    print(number)





theater_square()


