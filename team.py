


def team():


    num_problems = int(input())


    problems = 0
    for _ in range(num_problems):

        s = input()
        one_count = s.count('1')
        if one_count >= 2:
            problems += 1


    
    print(problems)

team()
        

