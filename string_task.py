


def string_task():


    s = input() 


    new_string = []
    
    
    vowels = {'A','E','I','O','U','Y'}

    for vowel in vowels.copy():
        vowels.add(vowel.lower())

    for character in s:
        if character not in vowels:
            if character.isupper():
                character = character.lower()
            new_string.append(f'.{character}')


    print(''.join(new_string))



string_task()




