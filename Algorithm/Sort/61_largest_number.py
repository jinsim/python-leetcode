""" 61. 가장 큰 수 (504) - 179
항목들을 조합해서 만들 수 있는 가장 큰 수를 출력하라.

Input: nums = [3,30,34,5,9]
Output: "9534330"
"""

class Solution:
    # 문제에 적합한 비교함수
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                print(i, j)
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))
