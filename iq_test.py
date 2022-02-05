from collections import Counter

def iq_test():


    odd_count = even_count = 0


    num_numbers = int(input())


    numbers = list(map(int,input().split()))


    counts = Counter(number % 2 == 0 for number in numbers[:3])
    

    if counts[True]  > 1:
        f = lambda x: x % 2 == 1
    else:
        f = lambda x: x % 2 == 0


    
    for i,number in enumerate(numbers,1):
        if f(number): 
            print(i)
            break


iq_test()
