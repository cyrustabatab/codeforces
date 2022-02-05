import math


def bear_and_big_brother():


    a,b = map(int,input().split())


    
    years = int(math.floor(math.log(b/a) / math.log(3/2)) + 1)


    print(years)




bear_and_big_brother()
