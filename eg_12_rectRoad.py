"""
设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径
路径可以从矩阵中的任意一格开始，每步可以在矩阵中向左右上下移动一格
如果一条路径经过了矩阵某一格，那么该路径不能再次进入该格子
"""
def rectRoad(rect,string):
    if rect is None or string is None:
        return False
    
    row = len(rect)
    col = len(rect[0])
    k = 0
    # visit = [[0]*col]*row 浅拷贝
    visit = [[0 for i in range(col)] for i in range(row)]

    for i in range(row):
        for j in range(col):
            if rectRoadcore(rect,row,col,i,j,string,k,visit):
                return True
    return False


def rectRoadcore(rect,row,col,i,j,string,k,visit):
    if len(string) == k:
        return True

    hasPath = False
    if i>=0 and j>=0 and i<row and j<col and rect[i][j]==string[k] and not visit[i][j]:
        k+=1
        visit[i][j] = 1

        hasPath = (rectRoadcore(rect,row,col,i-1,j,string,k,visit) or
        rectRoadcore(rect,row,col,i,j-1,string,k,visit) or 
        rectRoadcore(rect,row,col,i+1,j,string,k,visit) or
        rectRoadcore(rect,row,col,i,j+1,string,k,visit)) 

        if not hasPath:
            k -= 1
            visit[i][j] = 0

    return hasPath


print(rectRoad([['a','b','t','g'],['c','f','c','s'],['j','d','e','h']],'bfce'))

