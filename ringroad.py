from collections import Counter

def ringroad():


    n,m = map(int,input().split())

    
    
    tasks = list(map(lambda x: int(x)-1,input().split()))

    current_house  = 0
    time_taken = 0
    for i,task in enumerate(tasks):
        if i == 0 or task != tasks[i -1]:
            time = (task - current_house) % n
            time_taken += time
            current_house = task


    print(time_taken)


ringroad()










