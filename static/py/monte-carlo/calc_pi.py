import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import random
    def calc_pi(n):
        s = 0
        for _ in range(n):
            x = random.random()
            y = random.random()
            if x**2 + y**2 < 1:
                s += 1
        return s / n * 4


    print(calc_pi(1000000))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())