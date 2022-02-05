



def beautiful_year():


    year = int(input())

    
    def has_unique_digits(n):

        seen = set()

        while n:
            digit = n% 10
            if digit in seen:
                return False
            seen.add(digit)
            n //= 10

        return True
    
    year += 1
    while not has_unique_digits(year):
        year += 1

    
    print(year)


beautiful_year()




