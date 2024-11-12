def ternary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid1=left+(right-left)//3
        mid2=right-(right-left)//3
        if arr[mid1]==target:
            return mid1
        if arr[mid2]==target:
            return mid2
        if target<arr[mid1]:
            right=mid1-1
        elif target>arr[mid2]:
            left=mid2+1
        else:
            left=mid1+1
            right=mid2-1
    return -1
arr=[1,3,5,7,9,11,13,15]
target=int(input("Enter the number to find the position"))
result=ternary_search(arr,target)
if result!=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

