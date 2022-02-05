


def word():


    w = input()


    lower_count = 0 
    for c in w:
        if c.islower():
            lower_count += 1


    
    len_word = len(w)
    upper_count = len_word- lower_count


    if lower_count >= upper_count:
        print(w.lower())
    else:
        print(w.upper())
    

word()






