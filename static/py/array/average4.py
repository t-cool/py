import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def average(scores):
        sum_val = 0
        for i in range(len(scores)):
            sum_val += scores[i]
        return sum_val / len(scores)

    scores = [26, 78, 83, 20, 10, 11, 22, 16, 41, 95]
    print(average(scores))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())