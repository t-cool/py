import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def uniform_linear_motion(x0, v0, t):
        return x0 + v0 * t

    print(uniform_linear_motion(0, 10, 10))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())