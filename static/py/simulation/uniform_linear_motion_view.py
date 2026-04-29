import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import ita

    def draw_cell(x, y):
        image = [[0 for _ in range(100)] for _ in range(100)]
        image[len(image) - 1 - y][x] = 1
        return image


    def uniform_linear_motion_step(x, v0, dt):
        return x + v0 * dt


    def uniform_linear_motion(x0, v0, t, dt):
        x = []
        x.append(x0)
        n = int(t / dt)
        for i in range(n):
            x.append(uniform_linear_motion_step(x[i], v0, dt))
        return x


    # highlight-start
    x = uniform_linear_motion(0, 10, 10, 0.1)
    images = []
    for i in range(10):
        images.append(draw_cell(int(x[i * int(len(x) / 10)]), 50))
    ita.plot.animation_show(images)
    # highlight-end

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())