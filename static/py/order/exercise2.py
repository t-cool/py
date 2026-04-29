import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def calc_max(data):
        max_val = data[0]
        for i in range(1, len(data)):
            if max_val < data[i]:
                max_val = data[i]
        return max_val


    print(calc_max([1, 4, 3, 5, 2]))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())