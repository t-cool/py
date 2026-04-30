import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def prime_factorize(n):
        i = 2
        while n != 1:
            if n % i == 0:
                n /= i
                print(i)
            else:
                i += 1

    prime_factorize(24)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())