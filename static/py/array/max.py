import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def calc_max(scores):
        max_val = scores[0]
        for i in range(1, len(scores)):
            if max_val < scores[i]:
                max_val = scores[i]
        return max_val

    scores = [26, 78, 83, 20, 10, 11, 22, 16, 41, 95]
    print(calc_max(scores))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())