'''
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.
'''
#Brute Force Time: o(n^2) Space o(1 ) only variables i and j
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

#o(nlogn) space o( 1 )
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l,r = 0,1
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            l += 1
            r += 1
        return False
    
#just check adjacent 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

