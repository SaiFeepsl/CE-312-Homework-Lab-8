# Quick Sort
def quickSort(list_A,low,high):
    if high > low :
        pivot = partition(list_A,low,high)
        quickSort(list_A,low,pivot-1)
        quickSort(list_A,pivot+1,high)
        
        
def partition(list_A,low,high):
    pivot_item = list_A[low]
    
    left = low
    right = high
    while(left < right):
        while(list_A[left] <= pivot_item):
            left += 1
           
        
        while(list_A[right] > pivot_item):
            right -= 1
            
        if left < right :
            swap(list_A,left,right)
            
    
    list_A[low] = list_A[right]
    list_A[right] = pivot_item
    
    return right
def swap(list_A,left,right):
    temp = list_A[left]
    list_A[left] = list_A[right]
    list_A[right] = temp
    
    
list_A = [11,4,7,5,10,9,13,1]
n = len(list_A)
quickSort(list_A,0,n-1)
print("Sort list by QuickSort:\n " )
print(list_A)