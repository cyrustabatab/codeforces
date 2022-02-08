

def police_recruits():


    num_events =int(input())


    num_police = 0


    events = map(int,input().split())

    crimes = 0
    for event in events:
        if event == -1:
            if num_police == 0:
                crimes += 1
            else:
                num_police -= 1
        else:
            num_police += event



    print(crimes)


police_recruits()









