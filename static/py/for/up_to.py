import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def up_to(n):
        sum_val = 0
        for i in range(1, n + 1):
            sum_val += i
        return sum_val

    print(up_to(10))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())