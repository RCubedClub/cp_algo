# Python program for implementation of MergeSort 

# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 

#private merge fuction for merging array
def _merge(arr ,l ,m ,r):
    
    n1=m-l+1
    n2=r-m
    
    # create temp arrays 
    L=[0] * n1
    R=[0] * n2
    
    # Copy data to temp arrays L[] and R[] 
    for i in range(0,n1):
        L[i] = arr[l+i]
      
    for j in range(0,n2):
        R[j] = arr[m+j+1]
    
    # Merge the temp arrays back into arr[l..r] 
    k=l       # Initial index of merged subarray 
    i=0       # Initial index of first subarray 
    j=0       # Initial index of second subarray 
    while i<n1 and j<n2:
        if(L[i] <= R[j]):
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    
    
    # Copy the remaining elements of L[], if there are any        
    while i<n1:
        arr[k]=L[i]
        k+=1
        i+=1
    
    while j<n2:
        arr[k]=R[j]
        k+=1
        j+=1
#end of _merge function



#mergeSort function which is called from user program to sort array
def mergeSort(arr, l, r):
    
    
    if l<r:
        #avoid overflow
        m = l + (r-l)//2
        
        # Sort first and second halves 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        _merge(arr, l, m, r)

#emd of mergeSort function

        
          
        
        
