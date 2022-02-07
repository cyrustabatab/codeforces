


def fox_and_snake():


    n,m = map(int,input().split())

    
    
    hashtags = '#' * m
    

    s1 = f'{"." * (m - 1)}#'
    s2 = f'#{"." * (m - 1)}'
    strings = [s1,s2]
    end = False
    for i in range(n):
        if i  % 2 == 0:
            print(hashtags)
        else:
            print(strings[end])
            end = not end



fox_and_snake()
