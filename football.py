


def football():


    s = input()


    previous = None
    count = 0
    for character in s:
        if character == previous:
            count += 1
            if count == 7:
                print('YES')
                break
        else:
            count =1

        previous = character
    else:
        print('NO')


football()
