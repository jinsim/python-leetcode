""" 86. 최대 서브 배열 (53) - 636
합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""
class Solution:
    #1 메모이제이션
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += (nums[i - 1] if nums[i - 1] > 0 else 0)
        return (max(nums))

    #2 카데인 알고리즘
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum