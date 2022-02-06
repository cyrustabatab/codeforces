


def vanya_and_lanterns():


    num_lanterns,length_of_street = map(int,input().split())



    locations = set(map(int,input().split()))

    locations = list(locations)
    locations.sort()

    max_distance = float("-inf")


    for i in range(1,len(locations)):
        distance = locations[i] - locations[i -1]
        max_distance = max(max_distance,distance/2)



    if locations[0] != 0:
        max_distance = max(locations[0],max_distance)

    if locations[-1] != length_of_street:
        max_distance = max(length_of_street - locations[-1],max_distance)


    print(max_distance)


vanya_and_lanterns()





