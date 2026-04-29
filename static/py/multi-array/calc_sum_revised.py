import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def calc_sum2d(scores):
        sum_val = 0
        for i in range(len(scores)):
            for j in range(len(scores[i])):
                sum_val += scores[i][j]
        return sum_val


    scores = [[83, 75, 32], [73, 53, 84], [63, 48, 64]]

    print(calc_sum2d(scores))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())