


def tram():


    stops = int(input())

    
    people = 0
    max_capacity =0
    for _ in range(stops):

        a,b = map(int,input().split())

        people -= a
        people += b
        max_capacity = max(people,max_capacity)


    print(max_capacity)


tram()


