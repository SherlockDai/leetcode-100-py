class Solution:
    def rotate(self, matrix):
        return self.rotate_layer(0, 0, len(matrix[0]), len(matrix), matrix)

    def rotate_layer(self, x, y, w, h, matrix):
        if w <= 1 and h <= 1:
            return matrix
        for row in range(0, h - 1):
            temp = matrix[x + row][y]
            matrix[x + row][y] = matrix[x][y + w - 1 - row]
            matrix[x][y + w - 1 - row] = matrix[x + h - 1 - row][y + w - 1]
            matrix[x + h - 1 - row][y + w - 1] = matrix[x + h - 1][y + row]
            matrix[x + h - 1][y + row] = temp
        return self.rotate_layer(x + 1, y + 1, w - 2, h - 2, matrix)


sol = Solution()
print(sol.rotate([[1,2,3, 4],[5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]]))