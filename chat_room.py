


def chat_room():

    s = input()


    word = "hello"

    word_index = 0


    for character in s: 
        if character == word[word_index]:
            word_index += 1
            if word_index == len(word):
                print('YES')
                break

    else:
        print('NO')

    
chat_room()
