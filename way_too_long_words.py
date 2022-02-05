



def way_to_long():

    n = int(input())


    for _ in range(n):
        word = input()

        length_word = len(word)

        if length_word > 10:
            print(f"{word[0]}{length_word - 2}{word[-1]}")
        else:
            print(word)


way_to_long()
