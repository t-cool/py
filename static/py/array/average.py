import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    score1 = 96
    score2 = 56
    score3 = 42
    score4 = 74
    score5 = 86
    print((score1 + score2 + score3 + score4 + score5) / 5)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())