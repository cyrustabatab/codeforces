import sys

def t_primes():



    n = int(sys.stdin.readline())


    numbers = map(int,sys.stdin.readline().split())
    

    def bs(number):

        low,high = 1,number

        while low <= high:
            mid = (low + high)//2

            if mid**2 == number:
                return mid


            if mid**2  < number:
                low = mid + 1

            else:
                high = mid - 1





        return low




    for number in numbers:
        if number != 1:

            if number % 2 == 1:
                square_root = bs(number)
                if square_root**2 == number:

                    s = bs(square_root)
                    # check if this number is prime

                    for i in range(2,s + 1):
                        if square_root % i == 0:
                            print('NO')
                            break
                    else:
                        print('YES')
                else:
                    print('NO')
            elif number == 4:
                print('YES')
            else:
                print('NO')

        else:
            print('NO')


t_primes()


