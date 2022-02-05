



def stones_on_the_table():


    length = int(input())


    s = input()

    
    longest_length = float("-inf")


    stones = 0
    i = 0

    while i < len(s):
        character = s[i]

        j = i + 1

        while j < len(s) and s[j] == character:
            j += 1

        length = j - i
        
        i = j
        stones += length -1  



    print(stones)





stones_on_the_table()
