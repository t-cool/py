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
            # highlight-next-line
            if data[center] < number:
                start = center
            else:
                end = center
        return end


    data = [1, 2, 3, 4, 5, 5, 7, 8, 10]
    print(binary_search(data, 5))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())