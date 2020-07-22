# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    
    merged_arr = []

    # Your code here
   while a <len(arrA) and b < len(arrB):
       if arrA[a] < arrB[b]:
           merged_arr.extend(arrA[a:])
        if 
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # first i will check if the arr has more than one value
    if len(arr) == 1:
    # if it does not return 
        return
    # check if value is even'
    # if its even split the array evenly
    
    
    # else split and give oneside an extra value
    # return recurssive(left) return recursive(right)
   
    arr = mergedleft + mergedright


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

