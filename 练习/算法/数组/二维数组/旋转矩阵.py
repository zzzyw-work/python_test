'''
旋转矩阵
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

copy.deepcopy深拷贝的方法
矩阵的旋转方法

'''



#90°旋转是将[i][j]位置的值置换成[n-j-1][i]位置的值（n为长度）

class Solution:
    def rotate(self, matrix):
        import copy
        tmp=copy.deepcopy(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                tmp[i][j] = matrix[n-j-1][i]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = tmp[i][j]
if __name__ == "__main__":
    matrix =[
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    demo = Solution()
    demo.rotate(matrix)
    print(matrix)