# def binary_search(arr, target, start, end):
#     # Your code here
#     # First I would want to check if the array
#     # has a value if not return the function
    
#     if start != len(arr):
#         if arr[0] == target:
#             return True
#         else:
#             x = start + 1
#             return binary_search(arr[start:],target,x,end )
#     else:
#         return False
        
        
            
        

# ln=[4,2,1,-5]

# print(binary_search(ln,5,0,4))

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    
    merged_arr = []

    # Your code here
    for i in range(elements -2 ) :
        if arrA[i]<arrB[i]:
            merged_arr.append(arrA[i])
        if arrB[i]<arrA[i]:
            merged_arr.append(arrB[i])
        
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # first i will check if the arr has more than one value
    if len(arr) <= 1:
    # if it does not return 
        return
    # check if value is even'
    # if its even split the array e_svenly
    mid = len(arr) //2
    
    left = arr[:mid -1]
    right= arr[mid + 2:]
    
    n = merge_sort(left)
    
    # else split and give oneside an extra value
    # return recurssive(left) return recursive(right)
   
    arr = merge


    return left,mid,right

nn = [33,12,55,66,4,3,5,22,43,74]

print(merge_sort(nn))