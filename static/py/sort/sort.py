import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    data = [3, 8, 2, 5, 1, 10, 6, 9, 4, 7]
    data.sort()
    print(data)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())