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



# The function toHex takes an integer num as input and returns a string representing the hexadecimal value of num.

# To handle negative numbers, check if num is less than 0. If it is, add 2**32 to num to convert it to its equivalent positive value.

# The variables result and hex_digits are initialized. result will store the hexadecimal representation of num, and hex_digits is a string containing the valid hexadecimal digits.

# Enters a while loop that continues until num is greater than or equal to 16 (the base of the hexadecimal system).

# Inside the loop, calculate the remainder (reminder) of num divided by 16, which gives the value of the current hexadecimal digit. The remainder is then used to access the corresponding character from the hex_digits string.

# The character is appended to the result string.

# num is updated by performing integer division (num //= 16) to remove the least significant digit.

# Once the loop finishes, the code appends the last remaining digit (num) to the result string.

# Finally, the result string is reversed using the slice result[::-1] to get the correct order of hexadecimal digits, and it is returned as the final result.

# The algorithm used is a straightforward approach to convert a number from base 10 to base 16 (hexadecimal).It repeatedly calculates the remainder and performs integer division to obtain the digits in reverse order. Use hex_digits string instead of list 
