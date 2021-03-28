
def bubbleSort(list_to_sort, dec=0):
    length = len(list_to_sort)
    for i in range(0, length-1):
        for j in range(0, length-i-1): 
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]

    if dec:
        list_to_sort.reverse()
    return list_to_sort



