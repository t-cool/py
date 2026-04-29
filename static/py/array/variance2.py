import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def average(scores):
        sum = 0
        for i in range(len(scores)):
            sum += scores[i]
        return sum / len(scores)


    def variance(scores):
        sum = 0
        for i in range(len(scores)):
            sum += (scores[i] - average(scores)) ** 2
        return sum / len(scores)


    scores = [26, 78, 83, 20, 10, 11, 22, 16, 41, 95]
    print(variance(scores))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())