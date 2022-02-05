


def wanna_be_the_guy():


    n = int(input())

    
    _,*levels =map(int,input().split())

    levels = set(levels)

    
    y_levels = map(int,input().split())

    next(y_levels)


    for level in y_levels:
        levels.add(level)

    if len(levels) == n:
        print('I become the guy.')
    else:
        print('Oh, my keyboard!')


wanna_be_the_guy()



