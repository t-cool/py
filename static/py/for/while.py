import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    sum_val = 0
    i = 1
    while i <= 10:
        sum_val += i
        i += 1
    print(sum_val)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())