"""
在二维数组中，每行从左到右递增，每列从上到下递增，指定一个整数是否在数组中
"""

def find(nums,k):
    row = len(nums)
    col = len(nums[0])

    for i in range(row):
        if col == 1 and nums[i][0] > k:
            break
        for j in range(col):
            if nums[i][j] == k:
                return True
            elif nums[i][j] > k:
                col = j
                break
        
    return None


print(find([[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]], 6.0))



####################################
class Solution:
    # array 二维列表
    def Find(self, array, target):
        # 判断数组是否为空
        if array == []:
            return False

        rawnum = len(array)
        colnum = len(array[0])

        # 判断非法输入
        # 可以换成 isinstance(target, (int, float)) 进行判断
        if type(target) == float and type(array[0][0]) == int:
            if int(target) == target:
                return False
            target = int(target)
        elif type(target) == int and type(array[0][0]) == float:
            target = float(int)
        elif type(target) != type(array[0][0]):     # 浮点数的相等判断问题需要特别注意, 一般都是判断两个数的差值是否小于一个特别小的数。这里不展开分析。
            return False

        i = colnum - 1
        j = 0
        while i >= 0 and j < rawnum:
            if array[j][i] < target:
                j += 1
            elif array[j][i] > target:
                i -= 1
            else:
                return True
        return False
    # 扩展, 输出数组中target的个数
    def searchMatrix(self, matrix, target):
        if matrix == None or len(matrix) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        count = 0
        while row <= rows - 1 and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                count += 1
                col -= 1
        return count


array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
array2 = []
array3 = [['a', 'b', 'c'],
          ['b', 'c', 'd']]
array4 = [[62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],[63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],[64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],[66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],[67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]]


findtarget = Solution()
print(findtarget.Find(array, 10))
print(findtarget.Find(array, 30))
print(findtarget.Find(array, 13.0))
print(findtarget.Find(array, ''))
print(findtarget.Find(array2, 10))
print(findtarget.Find(array3, 'b'))
print(findtarget.searchMatrix(array4, 81))