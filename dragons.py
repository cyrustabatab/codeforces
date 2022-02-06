


def dragons():


    s,n = map(int,input().split())

    
    dragons = []
    for _ in range(n):
        dragon = tuple(map(int,input().split()))
        dragons.append(dragon)

   
    dragons.sort(key=lambda x:x[0])

    for dragon_strength,strength_gained in dragons:
        if s <= dragon_strength:
            print('NO')
            break

        s += strength_gained
    else:
        print("YES")

dragons()





