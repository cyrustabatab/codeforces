


def twins():


    num_coins = int(input())


    coin_values = list(map(int,input().split()))


    total_value = sum(coin_values)


    coin_values.sort(reverse=True)
    

    
    threshold = int(total_value /2 ) + 1
    cum_sum = 0


    for i,coin_value in enumerate(coin_values,1): 
        cum_sum += coin_value
        if cum_sum >= threshold:
            print(i)
            break



twins()
