def selection_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr
arr=[5,7,9,2,4,1]
print(selection_sort(arr))