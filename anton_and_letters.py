

def anton_and_letters():


    s = input()

    seen = set()
    for i in range(1,len(s) - 1):
        if s[i +1] in (',','}'):
            seen.add(s[i])



    
    print(len(seen))





anton_and_letters()
