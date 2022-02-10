"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

solution: 

so we can get the result of the problem with brute force.
as: 
    def subarraySum(nums, k):
        res = 0
        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                if curSum == k:
                    res += 1
        return res

but doing so it will take O(n^2) time and O(n) space.

so to reduce the time complexity we can use the prefix sum.

"""


def subarraySum(nums, k):
    res = 0
    curSum = 0
    preFix = {0: 1}

    for i in nums:
        curSum += i
        diff = curSum - k
        res += preFix.get(diff, 0)
        preFix[curSum] = preFix.get(curSum, 0) + 1
    return res


print(subarraySum([1, 1, 1], 2))
