import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import random
    def calc_dice_probability(n):
        one = 0
        for _ in range(n):
            if random.randint(1, 6) == 1:
                one += 1
        return one / n


    print(calc_dice_probability(100000))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())