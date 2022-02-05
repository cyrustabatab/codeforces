


def divisibility_problem():


    num_test_cases = int(input())


    for _ in range(num_test_cases):
        a,b = map(int,input().split())


        remainder = a % b
        
        if remainder != 0:
            remainder = b - remainder


        print(remainder)



divisibility_problem()


