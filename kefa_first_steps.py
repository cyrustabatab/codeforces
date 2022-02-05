


def kefa_first_steps():
    n = int(input())



    numbers = map(int,input().split())

    previous_number = float("inf")
    max_count = 0
    count = 0
    for number in numbers:
        if number < previous_number:
            max_count = max(max_count,count)
            count = 1
        else:
            count += 1
        previous_number = number

    
    max_count = max(count,max_count)
    print(max_count)



kefa_first_steps()
