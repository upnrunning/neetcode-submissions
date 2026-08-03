class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            symbol_left = s[left]
            symbol_right = s[right]
            if not symbol_left.isalnum():
                left += 1
                continue
            if not symbol_right.isalnum():
                right -= 1
                continue
            if symbol_left.lower() != symbol_right.lower():
                return False
            left += 1
            right -= 1
        return True