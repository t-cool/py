import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import math


    def is_prime_number(n):
        if n < 2:
            return False
        # highlight-next-line
        for i in range(2, math.floor(math.sqrt(n))):
            if n % i == 0:
                return False
        return True


    def print_prime_number(n):
        for i in range(1, n + 1):
            if is_prime_number(i):
                print(i)


    print_prime_number(100)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())