


def presents():
    


    num_friends = int(input())

    friends = map(int,input().split())

    mapping = {}
    for i,friend in enumerate(friends):
        mapping[(friend)] =  i + 1



    for i in range(1,num_friends + 1):
        print(mapping[i],end=' ')




presents()









