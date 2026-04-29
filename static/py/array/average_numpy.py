import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import numpy

    scores = [26, 78, 83, 20, 10, 11, 22, 16, 41, 95]
    print(numpy.mean(scores))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())