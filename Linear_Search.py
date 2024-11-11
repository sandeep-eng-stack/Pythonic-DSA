def find_two_numbers(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return f"Pair found: {arr[i]} and {arr[j]}"
    return "No pair found"
arr=[1,2,5,7,9,11,15]
target=int(input("Enter the number you want to find the index:"))
result=find_two_numbers(arr,target)
print(result)