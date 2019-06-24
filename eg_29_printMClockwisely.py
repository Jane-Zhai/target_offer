'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
def printMatrix(matrix):
    if matrix is None:
        return
    rows = len(matrix)
    cols = len(matrix[0])
    start = 0
    # 每次循环一圈，起始点为（start，start）
    while rows > start*2 and cols > start*2:
        printMatrixCW(matrix,cols,rows,start)
        start += 1
    print('')

def printMatrixCW(matrix,cols,rows,start):
    endx = cols - 1 - start
    endy = rows - 1 - start

    # 从左到右
    for i in range(start, endx+1):
        print(matrix[start][i],end=' ')
    # 从上到下
    if start < endy:
        for i in range(start+1, endy+1):
            print(matrix[i][endx],end=' ')
    
    # 从右到左打印一行
    if start < endx and start < endy:
        for i in range(endx-1, start-1, -1):
            number = matrix[endy][i]
            print(number, end=' ')

    # 从下到上打印一行
    if start < endx and start < endy-1:
        for i in range(endy-1, start, -1):
            number = matrix[i][start]
            print(number,end=' ')


def spiralOrder(matrix):
    return matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1])

matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1],[2],[3],[4],[5]]
matrix3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
spiralOrder(matrix)