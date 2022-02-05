


def helpful_maths():


    s = input()


    parts = s.split('+')



    start,high = -1,len(parts)
    current = 0


    while current < high:
        if parts[current] == '1': 
            parts[start +1] ,parts[current] = parts[current],parts[start + 1]
            current += 1
            start += 1
        elif parts[current] == '2':
            current += 1
        else:
            parts[high -1],parts[current]= parts[current],parts[high - 1]
            high -=1 



    
    print('+'.join(parts))


helpful_maths()









