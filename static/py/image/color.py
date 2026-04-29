import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import ita

    image = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
    ita.plot.image_show(image)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())