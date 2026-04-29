import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import bisect
    data = [1, 3, 3, 3, 4, 6, 8, 10, 10]

    print(bisect.bisect_right(data, 3))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())