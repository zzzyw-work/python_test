class solutionMethod:
    def bubble_sort(self,arr):
        n = len(arr)
        # 遍历所有数组元素
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
if __name__=="__main__":
    demo = solutionMethod()
    arr = [3, 2, 0, 7, 4]
    demo.bubble_sort(arr)
    print(arr)