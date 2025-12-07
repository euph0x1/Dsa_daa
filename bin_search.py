def binserch(arr, target):
    low=0
    high=len(arr)-1

    while low<= high:
        mid=(low+high)//2
        if arr[mid] ==target:
            return mid
        elif arr[mid] < target:
            low= mid +1
        else:
            high=mid-1

print("enter elements: ", flush=True)
arr=list(map(int, input().split()))

print("got array")
print("enter target", flush=True)

target=int(input())
key=binserch(arr, target)
if key is not None:
    print(key)
else:
    print("target not in list ")

    
