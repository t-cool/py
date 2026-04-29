import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import random
    def calc_coin_probability(n):
        head = 0
        for _ in range(n):
            if random.randint(0, 1) == 1:
                head += 1
        return head / n


    print(calc_coin_probability(100000))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())