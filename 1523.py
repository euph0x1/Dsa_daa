#1523. Count Odd Numbers in an Interval Range
'''Given two non-negative integers low and high. 
Return the count of odd numbers between low and high (inclusive).

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].'''

#74/84 TCP
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        while low<=high:
            if low%2!=0:
                count=count+1
            low=low+1
        return count

#accepted
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total=high-low+1
        if total%2==0:
            return total//2
        else:
            if low%2==0:
               return total//2
            else:
                return (total//2)+1
        


    
