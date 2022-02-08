


def new_year_hurry():


    n,k = map(int,input().split())

    max_minutes = 240 - k


    low,high = 0,n


    while low <= high:

        mid = (low +high)//2

        
        time_taken = 5 * mid * (mid + 1)//2  
        if time_taken <= max_minutes:
            if 5 * (mid + 1) * (mid + 2)//2 > max_minutes:
                break


        if time_taken <= max_minutes:
            low = mid + 1
        else:
            high = mid -1 



    
    print(mid)





new_year_hurry()
