import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def binary_search(data, number):
        start, end = -1, len(data)
        while end - start > 1:
            center = (start + end) // 2
            if data[center] < number:
                start = center
            else:
                end = center
        return end

    data = [2, 10, 23, 37, 51, 57, 66, 88, 95]

    print(binary_search(data, 51) + 1)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())