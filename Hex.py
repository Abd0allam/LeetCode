class Solution:
    def toHex(self, num: int) -> str:
        # converting negative numbers to their equivalent positive values.
        if num < 0: num = num + 2**32
        result , hex_digits= '' , '0123456789abcdef'
        while num >= 16:
            reminder = num % 16
            result += str(hex_digits[reminder])
            num //= 16
        result += hex_digits[num]
        return result[::-1]
    
n=-1
o=Solution().toHex(n)
print(o)