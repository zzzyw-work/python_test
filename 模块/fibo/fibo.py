class fibo():
    def fib2(self,n): # 返回到 n 的斐波那契数列
        result = []
        a, b = 0, 1
        while b < n:
            result.append(b)
            a, b = b, a+b
        return result