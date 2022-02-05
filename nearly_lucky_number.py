


def nearly_lucky_number():


    number = int(input())

    
    count = 0
    while number:
        digit = number % 10
        if digit in (4,7):
            count += 1

        number //= 10


    if count in (4,7):
        print("YES")
    else:
        print('NO')



nearly_lucky_number()
