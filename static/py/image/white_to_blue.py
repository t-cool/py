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
            right_color = [0, 0, 1]
            left_color = [1, 1, 1]
            row.append(
                [
                    (left_color[0] * (n - 1 - j) + right_color[0] * j) / (n - 1),
                    (left_color[1] * (n - 1 - j) + right_color[1] * j) / (n - 1),
                    (left_color[2] * (n - 1 - j) + right_color[2] * j) / (n - 1),
                ]
            )
        image.append(row)
    ita.plot.image_show(image)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())