def find_two_numbers(arr,target):
    left,right=0,len(arr)-1
    while left<right:
        current_sum=arr[left]+arr[right]
        if current_sum==target:
            return arr[left],arr[right]
        elif current_sum<target:
            left=left+1
        else:
            right=right-1
    return None
arr=[20,30,40,50,60,70,80,90,100]
target=int(input("Enter the target:"))
result=find_two_numbers(arr,target)
print("Pair found:",result)