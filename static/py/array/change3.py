import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    scores = [96, 56, 42, 74, 86]
    i = 1
    laterScore = 37
    scores[i - 1] = laterScore
    print(scores)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())