#quick sort

#partition

#main quick sort function

def quick_sort(arr):
    if (len(arr) < 2):
        return arr
    else if (len(arr) == 2)
        
    else:
        pivot = arr[0]
        rest_of_arr = arr[1:]
        less = [ arr[i] for i in rest_of_arr if arr[i] <= pivot]
        greater = [ arr[i] for i in rest_of_arr if arr[i] > pivot] 
        return quick_sort(less) + [pivot] + quick_sort(greater)
    

#arr length has to be greater than 2
def partition(arr):
    i = 0
    pivot = arr[-1]
    j = len(arr) - 2

    while ( i < j):
        if (arr[i] > pivot):
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else: 
            i += 1
    
    if (arr[i] > pivot):
        arr[i], arr[-1] = arr[-1], arr[i]
        return i
    else:
        arr[i+1], arr[-1] = arr[-1], arr[i+1]
        return i+1



testarray = [1,2,3,4,5]
partition(testarray)
        
    




