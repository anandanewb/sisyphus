# Replace oldsubstr with newsubstry without using the startswith or endswith methods
def findAndReplace(text, oldsubstr, newsubstr):
    newtext = "" 
    text_i = 0
    old_i = 0
    while text_i < len(text):
        if text[text_i] == oldsubstr[old_i]:
            old_i += 1
            if old_i == len(oldsubstr):
                old_i = 0
            newtext += newsubstr
            text_i += len(oldsubstr)
        else:
            newtext += text[text_i]
            text_i += 1
    return newtext

def findAndReplaceList(lst, old_sublist, new_sublist):
    result = []
    i = 0
    while i < len(lst):
        if lst[i:i+len(old_sublist)] == old_sublist:
            result.extend(new_sublist)
            i += len(old_sublist)
        else:
            result.append(lst[i])
            i += 1
    return result

def myQuickSort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return myQuickSort(less) + [pivot] + myQuickSort(greater)
    
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Usage
def inplace_quicksort(arr):
    quicksort(arr, 0, len(arr) - 1)
    return arr


# multiple assert statements to test the function
assert findAndReplace("hello world", "hello", "goodbye") == "goodbye world"
assert findAndReplace("hello world", "world", "python") == "hello python"
assert findAndReplace("hello world", "hello", "hi") == "hi world"
assert findAndReplace("hello world", "world", "universe") == "hello universe"
assert findAndReplace("hello world there", "there", '') == "hello world "
assert findAndReplace(" ", " ", "hello world") == "hello world"