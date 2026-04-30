import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    G = 6.7 * 10 ** (-11)

    def F(r, M, m):
        return G * M * m / r**2

    F(2, 60, 20)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())