def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
arr=[2,5,4,7,1,9,13,15,51,11]
sorted_arr=bubble_sort(arr)
print(sorted_arr)
  
