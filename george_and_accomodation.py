


def george_and_accomodation():


    num_rooms = int(input())
    

    can_live_in = 0
    for _ in range(num_rooms):
        people,capacity = map(int,input().split())

        if people + 2 <= capacity:
            can_live_in += 1


    print(can_live_in)


george_and_accomodation()


