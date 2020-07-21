def binary_search(arr, target, start, end):
    # Your code here
    # First I would want to check if the array
    # has a value if not return the function
    
    if start != len(arr):
        if arr[0] == target:
            return True
        else:
            x = start + 1
            return binary_search(arr[start:],target,x,end )
    else:
        return False
        
        
            
        

ln=[4,2,1,-5]

print(binary_search(ln,-5,0,4))