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

    def parabolic_motion(v0, theta, t, dt):
        result = []
        n = int(t / dt)
        for i in range(n):
            t = dt * i
            result.append(
                [v0 * t * math.cos(theta), -1 / 2 * g * t**2 + v0 * t * math.sin(theta)]
            )
        return result

    result = parabolic_motion(30, math.pi / 4, 4, 0.01)
    images = []
    for i in range(10):
        images.append(
            draw_cell(
                int(result[i * int(len(result) / 10)][0]),
                int(result[i * int(len(result) / 10)][1]),
            )
        )
    ita.plot.animation_show(images)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())