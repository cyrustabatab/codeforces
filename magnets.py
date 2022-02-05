

def magnets():


    n = int(input())
    
    count = 0
    for i in range(n):
        value = input()
        if i == 0 or value[0] == previous_value[1]:
            count += 1

        previous_value = value
    print(count)

magnets()
