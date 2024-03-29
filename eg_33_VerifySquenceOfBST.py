'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。

假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''
def VerifyBST(nums):
    if not nums:
        return False
    root = nums[-1]
    index = 0

    for num in nums[:-1]:
        if num > root:
            break
        index += 1

    for num in nums[index:-1]:
        if num < root:
            return False

    left = True
    if index>0:
        left = VerifyBST(nums[:index])
    right = True
    if index<len(nums)-1:
        right = VerifyBST(nums[index:-1])

    return left and right
        

array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
print(VerifyBST(array))