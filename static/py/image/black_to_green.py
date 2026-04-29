import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import ita

    n = 100
    image = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append([0, j / (n - 1), 0])
        image.append(row)
    ita.plot.image_show(image)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())