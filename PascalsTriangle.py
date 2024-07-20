import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [math.comb(i, j) for j in range(i + 1)]
            triangle.append(row)
        return triangle