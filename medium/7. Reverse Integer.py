#SOLUTION

class Solution(object):
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            if result > (INT_MAX - digit) / 10:
                return 0
            
            result = result * 10 + digit
        
        return sign * result
