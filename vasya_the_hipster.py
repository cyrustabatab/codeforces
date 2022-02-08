


def hipster():


    red,blue = map(int,input().split())


    minimum = min(red,blue)


    red -= minimum
    blue -= minimum


    remaining = red if blue == 0 else blue


    same = remaining//2

    print(minimum,same)



hipster()



