""" 83. 과반수 엘리먼트 (169) - 610
과반수를 차지하는 엘리먼트를 출력하라.

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    #1 브루트포스를 이용한 풀이
    def majorityElement(self, nums: List[int]) -> int:
        # 끝까지 갔을 때 반환
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        # 절반씩 넣어서 재귀호출한다.
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        # a가 과반이 넘으면 a를 반환한다.
        return [b, a][nums.count(a) > half]

    #2 DP를 이용한 풀이
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num
    
    #3 분할정복을 이용한 풀이
    def majorityElement(self, nums: List[int]) -> int:
        # 끝까지 갔을 때 반환
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        # 절반씩 넣어서 재귀호출한다.
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        # a가 과반이 넘으면 a를 반환한다.
        return [b, a][nums.count(a) > half]
    
    #4 파이썬다운 방식
    def majorityElement(self, nums: List[int]) -> int:
	    return sorted(nums)[len(nums)//2]
