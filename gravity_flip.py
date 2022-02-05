

def gravity_flip():


    num_columns = int(input())


    amounts = list(map(int,input().split()))


    amounts.sort()


    print(' '.join(map(str,amounts)))



gravity_flip()
