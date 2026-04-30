import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def calc_sum1d(scores):
        sum_val = 0
        for i in range(len(scores)):
            sum_val += scores[i]
        return sum_val

    a_scores = [83, 75, 32]
    b_scores = [73, 53, 84]
    c_scores = [63, 48, 64]

    print(calc_sum1d(a_scores) + calc_sum1d(b_scores) + calc_sum1d(c_scores))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())