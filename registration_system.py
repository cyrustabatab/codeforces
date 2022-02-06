from collections import defaultdict

def registration_system():

    
    names = defaultdict(int)
    n = int(input())


    for _ in range(n):
        name = input()

        if name in names:
            length = names[name]
            print(f"{name}{length}")
        else:
            print('OK')

        names[name] += 1



registration_system()
