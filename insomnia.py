import math



def insomia():


    k,l,m,n,d = (int(input()) for _ in range(5))
    numbers = [k,l,m,n]


    count = 0
    for i in range(1,d + 1):
        if any(i % number == 0 for number in numbers):
            count += 1

    
    print(count)



insomia()




