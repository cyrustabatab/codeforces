

def bit():


    num_operations = int(input())

    
    x = 0
    for _ in range(num_operations):

        operation = input()

        if operation[0] == 'X':
            s = operation[1:]
        else:
            s = operation[:-1]


        if s == '++':
            x += 1
        else:
            x -= 1


    print(x)


bit()




