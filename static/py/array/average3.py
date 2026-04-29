import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    scores = [96, 56, 42, 74, 86]
    sum_val = 0
    for i in range(len(scores)):
        sum_val += scores[i]
    print(sum_val / 5)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())