


def even_odds():


    n,k = map(int,input().split())
    

    if n % 2 == 1:
        threshold = n //2 + 1
    else:
        threshold = n//2

    if k <= threshold:
        number = 2 * (k - 1) + 1
    else:
        remaining =  k - threshold
        number = 2 * (remaining)


    print(number)


even_odds()
