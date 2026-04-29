import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import ita

    def calc_weighted_mean(top_left, top_right, bottom_left, bottom_right, s, t):
        return (top_left * (1 - s) + top_right * s) * (1 - t) + (
            bottom_left * (1 - s) + bottom_right * s
        ) * t


    image = []
    n = 100
    for i in range(n):
        row = []
        for j in range(n):
            top_left = [1, 1, 1]
            top_right = [1, 0, 0]
            bottom_left = [0, 1, 0]
            bottom_right = [0, 0, 1]
            row.append([0, 0, 0])
            for k in range(3):
                row[j][k] = calc_weighted_mean(
                    top_left[k],
                    top_right[k],
                    bottom_left[k],
                    bottom_right[k],
                    j / (n - 1),
                    i / (n - 1),
                )
        image.append(row)

    ita.plot.image_show(image)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())