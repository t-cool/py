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


    def parabolic_motion_step(x, y, u, v, dt):
        x = x + u * dt
        y = y + v * dt
        u = u
        v = v - g * dt
        return [x, y, u, v]


    def parabolic_motion(v0, theta, t, dt):
        x = 0
        y = 0
        u = v0 * math.cos(theta)
        v = v0 * math.sin(theta)
        result = []
        result.append([x, y, u, v])
        n = int(t / dt)
        for i in range(n):
            result.append(
                parabolic_motion_step(
                    result[i][0], result[i][1], result[i][2], result[i][3], dt
                )
            )
        return result


    # highlight-start
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
    # highlight-end

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())