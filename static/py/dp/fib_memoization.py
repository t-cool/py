import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    memo = [-1 for _ in range(10000)]


    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif memo[n] != -1:
            return memo[n]
        else:
            memo[n] = fib(n - 1) + fib(n - 2)
            return fib(n - 1) + fib(n - 2)


    print(fib(100))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())