



def boy_or_girl():


    username = input()


    seen =set()


    for character in username:
        if character not in seen:
            seen.add(character)


    if len(seen) % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')



boy_or_girl()
