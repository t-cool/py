import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def uniform_linear_motion_step(x, v0, dt):
        return x + v0 * dt

    def uniform_linear_motion(x0, v0, t, dt):
        x = x0
        n = int(t / dt)
        for i in range(n):
            x = uniform_linear_motion_step(x, v0, dt)
        return x

    print(uniform_linear_motion(0, 10, 10, 0.1))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())