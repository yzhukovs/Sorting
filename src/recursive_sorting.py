# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    for i in range( 0, elements ):
        if a >= len(arrA):    # merged arrA
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  #  merged arrB
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  
            # if element in arrA smaller, adding to marged final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  
            merged_arr[i] = arrB[b]
            b += 1
             #or next element in arrB should be smaller and add to the merged array
    return merged_arr
    


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr [0 : len(arr) // 2])
        right = merge_sort(arr [len(arr) // 2 :])
        arr = merge(left, right )
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
