class Solution:
    def reverseBits(self, n: int) -> int:
        def convertBinary(num):
            if num == 0:
                return "0"

            binary_string = ""
            while num > 0:
                remainder = num % 2
                binary_string = str(remainder) + binary_string
                num //= 2
            binary_string = binary_string.zfill(32)
            return binary_string
        
        binary = convertBinary(n)
        rev_binary = binary[::-1]
        rev_int = int(rev_binary, 2)
        return rev_int