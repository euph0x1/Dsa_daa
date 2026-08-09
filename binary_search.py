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

    ==================================================
                BINARY SEARCH
==================================================

REQUIREMENT:
Array must be SORTED.

IDEA:
Compare with middle element and eliminate
half of the search space each time.


TIME COMPLEXITY:

Best Case:
O(1)

Average Case:
O(log n)

Worst Case:
O(log n)


SPACE:

Iterative:
O(1)

Recursive:
O(log n)   // due to recursion stack


MAX COMPARISONS:

Approximately:

ceil(log2(n))

For n = 1000:

log2(1000) ≈ 9.966

ceil(9.966) = 10

Therefore:

MAX COMPARISONS = 10


IMPORTANT POWERS:

2^9  = 512
2^10 = 1024

Since:

512 < 1000 < 1024

→ 10 comparisons


MEMORY TRICK:

Binary Search = "HALVE"

n → n/2 → n/4 → n/8 → ...

Therefore:

Number of steps ≈ log2(n)
==================================================