==================================================
                INSERTION SORT
==================================================

IDEA:
Insertion Sort builds the sorted array one element
at a time.

Think of arranging playing cards in your hand.

At every step:
    1. Take the next element → key
    2. Compare key with elements on its left
    3. Shift elements greater than key one position right
    4. Insert key into its correct position


EXAMPLE:
Array = [5, 3, 4, 1]

Start:
[5] | [3, 4, 1]
 ↑
sorted portion

Take 3:
[5, 3]
3 < 5 → shift 5
[3, 5]

Take 4:
[3, 5, 4]
4 < 5 → shift 5
[3, 4, 5]

Take 1:
[3, 4, 5, 1]
1 < 5 → shift
1 < 4 → shift
1 < 3 → shift
[1, 3, 4, 5]


--------------------------------------------------
PSEUDOCODE
--------------------------------------------------

for i = 1 to n-1:
    key = A[i]
    j = i - 1

    while j >= 0 AND A[j] > key:
        A[j+1] = A[j]       // shift
        j = j - 1

    A[j+1] = key            // insert


--------------------------------------------------
PYTHON CODE
--------------------------------------------------

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [5, 3, 4, 1, 2]
print(insertion_sort(arr))


OUTPUT:
[1, 2, 3, 4, 5]


--------------------------------------------------
TIME COMPLEXITY
--------------------------------------------------

BEST CASE:
Array already sorted

Example:
[1, 2, 3, 4, 5]

Comparisons ≈ n - 1

Time = O(n)


AVERAGE CASE:

Elements are randomly ordered

Time = O(n²)

WORST CASE:
Array is reverse sorted

Example:
[5, 4, 3, 2, 1]

Every element must move through the
sorted portion.

Time = O(n²)


--------------------------------------------------
SPACE COMPLEXITY
--------------------------------------------------

O(1)

Insertion Sort is an IN-PLACE algorithm.


--------------------------------------------------
IMPORTANT PROPERTIES
--------------------------------------------------

✓ Stable
✓ In-place
✓ Adaptive
✓ Good for small arrays
✓ Very good for nearly sorted arrays
✓ Simple to implement


--------------------------------------------------
INSERTION SORT + INVERSIONS
--------------------------------------------------

An inversion is a pair (i, j) where:

i < j AND A[i] > A[j]

Example:

[1, 2, 3, 5, 4]

Only inversion:
(5, 4)

Number of inversions = 1

For standard Insertion Sort:

Number of SHIFTS = Number of INVERSIONS


--------------------------------------------------
COMPARISON FORMULAS
--------------------------------------------------

BEST CASE:

N = n - 1

WORST CASE:

Approximately:

N = 1 + 2 + 3 + ... + (n-1)

    = n(n-1)/2

IMPORTANT:
Exact comparison count can depend on the
implementation and whether the final failed
comparison is counted.


--------------------------------------------------
SWAP vs SHIFT
--------------------------------------------------

Standard Insertion Sort uses SHIFTING,
not swapping.

Example:

[1, 2, 3, 5, 4]

key = 4

Shift 5:

[1, 2, 3, 5, 5]

Insert 4:

[1, 2, 3, 4, 5]

So this is:

1 SHIFT + 1 INSERTION

not necessarily 1 SWAP.


--------------------------------------------------
QUICK COMPARISON
--------------------------------------------------

                 BEST       AVG        WORST
------------------------------------------------
Insertion Sort   O(n)      O(n²)      O(n²)
------------------------------------------------

Space: O(1)
Stable: YES
In-place: YES
Adaptive: YES


KEY MEMORY TRICK:

INSERTION SORT =
"Take → Compare → Shift → Insert"

Best → Already sorted → O(n)
Worst → Reverse sorted → O(n²)
Space → O(1)
Stable → YES
==================================================