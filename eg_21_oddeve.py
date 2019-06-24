"""
题目：调整数组的顺序使奇数位于偶数前面
题一：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""
def swap(alist):
    front = 0
    last = len(alist)-1

    while front<last:
        if alist[front] & 0x1 == 0:
            if alist[last] & 0x1 != 0:
                temp = alist[front]
                alist[front] = alist[last]
                alist[last] = temp
            else:
                last -= 1
        else:
            front += 1
    return alist

print(swap([1,4,5,2,3,8,7]))

class Solution:
    def reOrderArray(self, array):
        # write code here
        if array==None or len(array)==0:
            return
        pBegin=0
        pEnd=len(array)-1
        while (pBegin<pEnd):
            while pBegin<pEnd and not self.isEven(array[pBegin]):
                pBegin += 1
            while pBegin<pEnd and self.isEven(array[pEnd]):
                pEnd -= 1
            if pBegin<pEnd:
                temp=array[pBegin]
                array[pBegin]=array[pEnd]
                array[pEnd]=temp
        return array

    def isEven(self,number):
        return number & 1==0