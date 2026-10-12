class Solution:
    def getRow(self, rowIndex):
        result = []
        for i in range(rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = result[j - 1] + result[j]
            result = row
        return result