import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    import math
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
        n = int(t / dt)
        for i in range(n):
            x, y, u, v = parabolic_motion_step(x, y, u, v, dt)
        return [x, y]


    print(parabolic_motion(30, math.pi / 4, 4, 0.01))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())