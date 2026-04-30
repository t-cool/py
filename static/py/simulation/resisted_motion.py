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

    def parabolic_motion_step(y, v, K, dt):
        y = y + v * dt
        v = v - g * dt - K * v * dt
        return [y, v]

    def parabolic_motion(K, t, dt):
        y = 100
        v = 0
        result = []
        result.append([y, v])
        n = int(t / dt)
        for i in range(n):
            result.append(parabolic_motion_step(result[i][0], result[i][1], K, dt))
        return result

    result = parabolic_motion(6, 60, 0.01)
    images = []
    for i in range(10):
        images.append(draw_cell(50, int(result[i * int(len(result) / 10)][0])))
    ita.plot.animation_show(images)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())