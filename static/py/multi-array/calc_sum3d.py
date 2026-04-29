import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def calc_sum3d(scores):
        sum_val = 0
        for i in range(len(scores)):
            for j in range(len(scores[i])):
                for k in range(len(scores[i][j])):
                    sum_val += scores[i][j][k]
        return sum_val


    scores = [[[51, 56, 10], [47, 52, 58]], [[24, 92, 34], [28, 44, 19]]]

    print(calc_sum3d(scores))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())