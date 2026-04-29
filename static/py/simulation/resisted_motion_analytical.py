import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import math

    import ita

    def draw_cell(x, y):
        image = [[0 for _ in range(100)] for _ in range(100)]
        image[len(image) - 1 - y][x] = 1
        return image


    g = 9.8


    def parabolic_motion(K, t, dt):
        result = []
        n = int(t / dt)
        for i in range(n):
            t = dt * i
            result.append((1 / K) ** 2 * g * (1 - math.exp(-K * t)) - (1 / K) * g * t + 100)
        return result


    result = parabolic_motion(6, 60, 0.01)
    images = []
    for i in range(10):
        images.append(draw_cell(50, int(result[i * int(len(result) / 10)])))
    ita.plot.animation_show(images)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())