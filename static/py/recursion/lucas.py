import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def lucas(n):
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return lucas(n - 1) + lucas(n - 2)


    print(lucas(10))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())