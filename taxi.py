from collections import Counter

def taxi():


    num_groups = int(input())



    group_sizes= map(int,input().split())

    

    counts = Counter(group_sizes)


    s = counts[4] + counts[3]
    # 3 three case 


    counts[1] -= min(counts[3],counts[1])



    # 2 case

    half = counts[2]//2
    s += half
    counts[2] -= half * 2

    
    if counts[2]:
        s += 1
        if counts[1] <= 2:
            counts[1] = 0
        else:
            counts[1] -= 2

    
    if counts[1]:
        remaining = counts[1]
        s += remaining // 4
        if remaining % 4 != 0:
            s += 1




    
    print(s)


    

















taxi()
