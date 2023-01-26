""" 62. 유효한 애너그램 (242) - 507
t가 s의 애너그램인지 판별하라.

Input: s = "anagram", t = "nagaram"
Output: true
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
