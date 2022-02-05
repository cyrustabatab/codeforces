


def arrival_general():

    num_soldiers = int(input())


    heights = map(int,input().split())


    minimum = float("inf")
    maximum =float("-inf")
    min_index = max_index = None


    for i,height in enumerate(heights):
        if height <= minimum:
            minimum = height
            min_index = i
        if height > maximum:
            maximum = height
            max_index = i


    
    num_soldiers -= 1
    operations = num_soldiers - min_index + max_index


    if min_index < max_index:
        operations -= 1

    
    print(operations)


arrival_general()
