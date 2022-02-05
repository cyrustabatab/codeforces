


def win_lottery():


    n = int(input())


    bill_sizes = [100,20,10,5,1]



    bills_used = 0 
    for bill_size in bill_sizes:
        if bill_size <= n:
            remaining = n % bill_size 
            used = n // bill_size

            bills_used += used


            n = remaining

            if n ==  0:
                break

    print(bills_used)



win_lottery()
















