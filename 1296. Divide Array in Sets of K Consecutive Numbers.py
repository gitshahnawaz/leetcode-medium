"""
1296. Divide Array in Sets of K Consecutive Numbers
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
 
"""



class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for i in sorted(nums):
            if d[i]>0:
                for j in range(k):
                    d[i+j] -= 1
        
        return len(set(list(d.values()))) == 1