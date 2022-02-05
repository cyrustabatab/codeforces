from collections import Counter


def amusing_joke():
    

    s = "NEW YEAR AND CHRISTMAS MEN"




    s1,s2,s3 = (input() for _ in range(3))

    letter_counts = Counter(s1)
    letter_counts.update(s2)


    for character in s3:
        letter_counts[character] -= 1
        if letter_counts[character] < 0:
            print("NO")
            break
    else:
        if all(value == 0 for value in letter_counts.values()):
            print("YES")
        else:
            print("NO")




amusing_joke()

