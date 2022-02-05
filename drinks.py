import math


def drinks():


    num_drinks = int(input())


    values = map(int,input().split())


    cum_sum = 0

    for value in values:
        cum_sum += value/100


    

    print(cum_sum/num_drinks * 100)



drinks()






