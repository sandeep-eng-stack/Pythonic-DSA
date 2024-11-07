def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[1,3,5,7,9,11,13]
target=int(input("Enter the element to find the index:"))
index=binary_search(arr,target)
print(f"Index of {target}:{index}" if index!=-1 else "Element Not Found")
