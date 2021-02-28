'''
数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
'''

class Solution():
    def findKthLargest(self,nums,k):
        """
        nums: List[int]
        k: int
        return:返回数组排序后的第k个最大的元素，不是第k个不同的元素；
        """
        # 查看输入内容是否符合要求
        if k >= 1 and k <= len(nums) and len(nums) > 0:
            nums_ = sorted(nums,reverse = True)
            result = nums_[k-1]
        else:
            print('error：输入内容不符合要求')
        return result
if __name__ == "__main__":
    demo = Solution()
    k=3
    nt = [45,98,-2,6,87,-9]
    result=demo.findKthLargest(nt, k)
    print(result)