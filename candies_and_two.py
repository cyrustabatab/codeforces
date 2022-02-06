


def candies_and_two():

    num_test_cases = int(input())


    for _ in range(num_test_cases):
        num_candies = int(input())

        if num_candies % 2 == 0:
            print(num_candies //2 -1)
        else:
            print(num_candies//2)


candies_and_two()
