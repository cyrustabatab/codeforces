from itertools import combinations




def expression():


    a,b,c = (int(input()) for _ in range(3))


    numbers = [a,b,c]

    total_sum = sum(numbers)
    mult = a * b * c

    results = [total_sum,mult]

    
    j = [-1,0]
    for i,j in zip(range(0,2),j):
        two = numbers[i:i+2]
        sum_and_mult = sum(two) * numbers[j]
        mult_and_sum = two[0] * two[1]  + numbers[j]
        results.append(sum_and_mult)
        results.append(mult_and_sum)



    result = max(results)

    print(result)


expression()

















