





def beautiful():

    
    center_x = center_y = 2
    for i in range(5):
        row = input()
        

        try:
            one_index = row.index('1') // 2
        except:
            pass
        else:
            diff_y =abs(one_index - center_x)
            diff_x = abs(i - center_y)
            print(diff_y + diff_x)
            break

        


beautiful()






