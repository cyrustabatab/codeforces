

def dubstep():

    s = input()

    

    i = 0
    
    original = []
    word= []
    while i < len(s):
        if s[i:i +3] == "WUB":
            if word:
                original.append(''.join(word))
                word = []
            i += 3
        else:
            word.append(s[i])
            i += 1

    
    if word:
        original.append(''.join(word))
    

    print(' '.join(original))




dubstep()



