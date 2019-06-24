'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1]
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''
def multiply(A):
    B = [1]*len(A)
    for i in range(1,len(A)):
        B[i] = B[i-1] * A[i-1]

    temp = 1
    for j in range(len(A)-2,-1,-1):
        temp *= A[j+1]
        B[j] *= temp
    return B