class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        k = m * n
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        bl = True
        while len(result) < m * n:
            if bl:
                for col in range(left, right + 1):
                    result.append(matrix[top][col])
                    top += 1
                    k -= 1
                if top <= bottom:
                    for row in range(top, bottom + 1):
                        result.append(matrix[row][right])
                    right -= 1


            else:
                if left <= right:
                    for col in range(right, left - 1, -1):
                        result.append(matrix[bottom][col])
                    bottom -= 1
                if top <= bottom:
                    for row in range(bottom, top - 1, -1):
                        result.append(matrix[row][left])
                    left += 1

            bl = not (bl)
        return result

sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))


