def search_2D(arr,target):
    m=len(arr)
    if m==0:
        return False
    n=len(arr[0])
    left,right=0,m*n-1
    while left<=right:
        mid=(left+right)//2
        mid_element=arr[mid//n][mid%n]
        if target==mid_element:
            return f"The element is present at row {mid//n} and coloumn {mid%n}"
        elif target>mid_element:
            left=mid+1
        else:
            right=mid-1
    return None
arr=[[1,2,3,4],[5,6,7,8],[12,13,14,15]]
target=int(input("Enter the number to find the position"))
print(search_2D(arr,target))







arr=[[1,2,3],[4,5,6],[7,8,9]]
target=int(input("Enter the number to find"))
serach_2D(array,target)
