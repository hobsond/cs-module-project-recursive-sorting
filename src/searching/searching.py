# TO-DO: Implement a recursive implementation of binary search

def binary_search(arr, target, start, end):
    # Your code here
    # First I would want to check if the array
    # has a value if not return the function
    
    if start != len(arr):
        if arr[0] == target:
            return 1
        else:
            x = start + 1
            return binary_search(arr[start:],target,x,end )
    else:
        return False
        
        
            
        


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

