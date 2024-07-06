class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        direction = -1
        k = 0

        for char in s:
            rows[k] += char
            if k==0 or k==(numRows - 1): # Check if Nth row is reached
                direction *= -1 # if so reversing the direction so text can be added in zigzag
            k += direction # k value will revolve around 0-2 (for numRows = 3)

        return ''.join(rows) 
