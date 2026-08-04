"""
=========================================================
                QUICK SORT - COMPLETE NOTES
=========================================================

Concept:
--------
Quick Sort is a Divide and Conquer algorithm.

Steps:
1. Choose a Pivot.
2. Partition the array.
3. Recursively sort left subarray.
4. Recursively sort right subarray.

In this implementation:
Pivot = First Element

=========================================================
"""

# -------------------------------------------------------
# Partition Function (First Element as Pivot)
# -------------------------------------------------------

def partition(arr, low, high):

    pivot = arr[low]

    left = low + 1
    right = high

    while True:

        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        if left > right:
            break

        arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]

    return right


# -------------------------------------------------------
# Quick Sort
# -------------------------------------------------------

def quicksort(arr, low, high):

    if low < high:

        pivot_index = partition(arr, low, high)

        quicksort(arr, low, pivot_index - 1)

        quicksort(arr, pivot_index + 1, high)


# -------------------------------------------------------
# Driver Code
# -------------------------------------------------------

arr = [7, 2, 1, 6, 8, 5, 3, 4]

print("Original Array:")
print(arr)

quicksort(arr, 0, len(arr)-1)

print("\nSorted Array:")
print(arr)


"""
=========================================================
                DRY RUN
=========================================================

Input:

[7,2,1,6,8,5,3,4]

Pivot = 7

Partition

[2,1,6,5,3,4] 7 [8]

Recursive calls

Left:
[2,1,6,5,3,4]

Right:
[8]

Again

Pivot = 2

[1] 2 [6,5,3,4]

Again

Pivot = 6

[5,3,4] 6 []

Eventually

[1,2,3,4,5,6,7,8]

=========================================================
                BEST CASE
=========================================================

Pivot always divides array equally.

Example:

[4,2,6,1,3,5,7]

Pivot = 4

Left:

[2,1,3]

Right:

[6,5,7]

Both halves almost equal.

Tree

            n

        /       \

      n/2      n/2

     /  \      /  \

   n/4 n/4  n/4 n/4

Height

log₂ n

Cost per level

O(n)

Recurrence

T(n)=2T(n/2)+O(n)

Time Complexity

O(n log n)

Space Complexity

O(log n)

=========================================================
                WORST CASE
=========================================================

Occurs when pivot is always smallest or largest.

Example (Already Sorted)

[1,2,3,4,5]

Pivot = 1

Left

[]

Right

[2,3,4,5]

Again

Pivot = 2

[]

[3,4,5]

Tree

n

↓

n-1

↓

n-2

↓

n-3

↓

1

Height

n

Cost per level

O(n)

Recurrence

T(n)=T(n-1)+O(n)

Time Complexity

O(n²)

Space Complexity

O(n)

=========================================================
                AVERAGE CASE
=========================================================

Pivot can land anywhere.

Example 1

40% - 60%

Example 2

20% - 80%

Example 3

50% - 50%

Example 4

75% - 25%

Every split is possible.

Average recurrence

                 n-1
T(n)= (1/n) Σ [T(k)+T(n-k-1)] + O(n)
                k=0

The partition always costs O(n).

Average Time Complexity

O(n log n)

Average Space Complexity

O(log n)

=========================================================
        WHY OPTION C IS CORRECT IN GATE?
=========================================================

Average case means

Pivot may become

Position 0

Position 1

Position 2

...

Position n-1

Each position is equally likely.

Therefore

Take average of ALL possible recursive calls.

Hence

(1/n) Σ(T(left)+T(right))+O(n)

=========================================================
                SUMMARY
=========================================================

Best Case

Balanced Partition

Example

50%-50%

Recurrence

T(n)=2T(n/2)+O(n)

Time

O(n log n)

Space

O(log n)

--------------------------------------------

Worst Case

Unbalanced Partition

Example

0%-100%

Recurrence

T(n)=T(n-1)+O(n)

Time

O(n²)

Space

O(n)

--------------------------------------------

Average Case

Random Pivot Position

Recurrence

(1/n)Σ(T(left)+T(right))+O(n)

Time

O(n log n)

Space

O(log n)

=========================================================
INTERVIEW NOTES
=========================================================

Advantages
----------
✔ Very fast in practice
✔ In-place sorting algorithm
✔ Cache friendly
✔ Average O(n log n)

Disadvantages
-------------
✘ Worst case O(n²)
✘ Not Stable

Stable?
-------
No

In-place?
----------
Yes

Divide and Conquer?
-------------------
Yes

=========================================================
"""