import string


def pangram():





    num_letters = int(input())


    if num_letters < 26:
        print('NO')
    else:
        letters = set(string.ascii_lowercase)
        s = input()

        for letter in s:
            lower = letter.lower()
            if lower in letters:
                letters.remove(lower)
                if not letters:
                    print("YES")
                    break
        else:
            print('NO')



pangram()
