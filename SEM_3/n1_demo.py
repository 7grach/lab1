from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m = len(matrix)  # количество строк
        n = len(matrix[0])  # количество столбцов

        # Границы
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        result = []
        bl = True  # True – прямой проход (верх+право), False – обратный (низ+лево)

        while len(result) < m * n:
            if bl:
                # --- Верхняя строка (слева направо) ---
                for col in range(left, right + 1):
                    result.append(matrix[top][col])
                top += 1  # верхняя граница опускается

                # --- Правый столбец (сверху вниз) ---
                # (если ещё есть строки)
                if top <= bottom:
                    for row in range(top, bottom + 1):
                        result.append(matrix[row][right])
                    right -= 1  # правая граница сдвигается влево
            else:
                # --- Нижняя строка (справа налево) ---
                # (если ещё есть столбцы)
                if left <= right:
                    for col in range(right, left - 1, -1):
                        result.append(matrix[bottom][col])
                    bottom -= 1  # нижняя граница поднимается

                # --- Левый столбец (снизу вверх) ---
                if top <= bottom:
                    for row in range(bottom, top - 1, -1):
                        result.append(matrix[row][left])
                    left += 1  # левая граница сдвигается вправо

            bl = not bl  # меняем направление на следующем витке

        return result

sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))