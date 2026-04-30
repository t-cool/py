import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def linear_search(data, number):
        for i in range(len(data)):
            # highlight-next-line
            if number <= data[i]:
                return i

    data = [1, 2, 3, 4, 5, 5, 7, 8, 10]
    print(linear_search(data, 5))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())