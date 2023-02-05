class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        reverse_number = 0
        temporary = x
        while temporary > 0:
            reverse_number = (reverse_number * 10) + (temporary % 10)
            temporary = temporary // 10
        if reverse_number == x :
            return True
        else:
            return False
