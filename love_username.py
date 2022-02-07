


def love_username():


    num_contests = int(input())

    points_earned = map(int,input().split())




    current_max = float("-inf")
    current_min = float("inf")

    amazing = 0
    current_max = current_min = next(points_earned)
    for point in points_earned:

        if point > current_max:
            amazing += 1
        if point < current_min:
            amazing += 1


        current_max =max(point,current_max)
        current_min = min(current_min,point)
    

    print(amazing)

love_username()














