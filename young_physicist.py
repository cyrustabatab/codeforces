from collections import defaultdict


def young():


    rows = int(input())

    
    col_sums = defaultdict(int)
    for _ in range(rows):

        values = map(int,input().split())

        for i,value in enumerate(values):
            col_sums[i] += value


    

    if all(col_sum == 0 for col_sum in col_sums.values()):
        print('YES')
    else:
        print('NO')



young()
