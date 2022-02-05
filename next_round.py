import random



def next_round():


    n,k = map(int,input().split())



    scores = list(map(int,input().split()))


    k = n - k - 1 # kth largest to kth smallest


    def quickselect(a):
    

        def partition(a,low,high):
            pivot_index = random.randint(low,high)

            pivot_value = a[pivot_index]
            a[low],a[pivot_index] = a[pivot_index],a[low]


            i = low + 1
            j = i


            while i <= high:
                if a[i] < pivot_value:
                    a[j],a[i] = a[i],a[j]
                    j += 1
                i += 1



            a[low],a[j -1] = a[j -1],a[low]

            return j -1






        
        def quickselect_helper(a,low,high,k):
            
            if low >= high:
                return a[high]

            p = partition(a,low,high)

            if p == k:
                return a[p]


            if k < p:
                return quickselect_helper(a,low,p -1,k)
            else:
                return quickselect_helper(a,p + 1,high,k)



        number =  quickselect_helper(a,0,len(a) - 1,k)
        return number
    

    number = quickselect(scores)

    print(sum( value > 0 and value >= number  for  value in scores))

def next_round_2():
    n,k = map(int,input().split()) 
    
    numbers = list(map(int,input().split()))
    

    advances = 0
    i = 0
    while i < len(numbers) and numbers[i] > 0 and numbers[i] >= numbers[k -1]:
        advances += 1
        i += 1


    print(advances)



next_round_2()






































