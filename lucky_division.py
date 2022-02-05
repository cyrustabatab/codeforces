import math


def lucky_division():


    n = int(input())


    lucky_digits = [4,7]


    

    def get_lucky_numbers(number,i=0):
        
        if number > n:
            return
        if number != 0:
            numbers.append(number)
        

        for digit in lucky_digits:
            number += 10**i * digit
            get_lucky_numbers(number,i + 1)
            number -= 10**i * digit



    
    numbers = []
    number = 0
    get_lucky_numbers(number)
    for lucky_number in numbers:
        if n % lucky_number  == 0:
            print('YES')
            break
    else:
        print("NO")


lucky_division()




