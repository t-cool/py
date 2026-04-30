import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def calc_sum(n):
        if n == 1:
            return 1
        else:
            return calc_sum(n - 1) + n

    print(calc_sum(10))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())