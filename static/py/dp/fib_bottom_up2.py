import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def fib(n):
        a, b = 0, 1
        if n == 0:
            return a
        if n == 1:
            return b
        for _ in range(n - 1):
            a, b = b, a + b
        return b

    print(fib(100))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())