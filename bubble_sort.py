def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [5,1,4,2,8]

bubble_sort(arr)

print(arr)

"""
=========================================================
                BUBBLE SORT - QUICK NOTES
=========================================================

Concept
-------
Bubble Sort repeatedly compares adjacent elements and
swaps them if they are in the wrong order.

After every pass, the largest unsorted element
"bubbles up" to its correct position.

---------------------------------------------------------
BEST CASE
---------------------------------------------------------

Condition
---------
Array is already sorted.

Example

[1, 2, 3, 4, 5]

Pass 1

1 < 2  ✓
2 < 3  ✓
3 < 4  ✓
4 < 5  ✓

No swaps occur.

Algorithm stops after the first pass
(using the swapped flag optimization).

Recurrence

T(n) = T(1) + O(n)

Time Complexity

O(n)

Space Complexity

O(1)

Reason
------
Only one traversal of the array is needed.

---------------------------------------------------------
AVERAGE CASE
---------------------------------------------------------

Condition
---------
Random order.

Example

[4, 2, 5, 1, 3]

Several swaps occur in each pass.

Time Complexity

O(n²)

Space Complexity

O(1)

---------------------------------------------------------
WORST CASE
---------------------------------------------------------

Condition
---------
Array is sorted in reverse order.

Example

[5, 4, 3, 2, 1]

Pass 1

5 4 3 2 1

↓

4 3 2 1 5

Pass 2

↓

3 2 1 4 5

Pass 3

↓

2 1 3 4 5

Pass 4

↓

1 2 3 4 5

Comparisons

(n-1) + (n-2) + ... + 2 + 1

= n(n-1)/2

Recurrence (Concept)

T(n) = T(n-1) + O(n)

Time Complexity

O(n²)

Space Complexity

O(1)

Reason
------
Every adjacent comparison results in a swap.

---------------------------------------------------------
SUMMARY
---------------------------------------------------------

Best Case

Already Sorted

Time  : O(n)
Space : O(1)

-----------------------------------------

Average Case

Random Order

Time  : O(n²)
Space : O(1)

-----------------------------------------

Worst Case

Reverse Sorted

Time  : O(n²)
Space : O(1)

---------------------------------------------------------
INTERVIEW POINTS
---------------------------------------------------------

✔ Stable Sorting Algorithm
✔ In-place Sorting Algorithm
✔ Adaptive (Optimized Version)
✔ Compares Adjacent Elements
✔ Largest Element reaches the end after every pass

=========================================================
"""