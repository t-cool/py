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

    # highlight-start
    def calc_total_score_max(scores):
        max_score = 0
        for i in range(len(scores)):
            total_score = calc_sum1d(scores[i])
            if max_score < total_score:
                max_score = total_score
        return max_score

    # highlight-end

    scores = [[83, 75, 32], [73, 53, 84], [63, 48, 64]]

    print(calc_total_score_max(scores))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())