import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def bubble_sort(data):
        n = len(data)
        for i in range(n):
            for j in range(i + 1, n):
                if data[i] > data[j]:
                    data[i], data[j] = data[j], data[i]
        return data


    data = [3, 8, 2, 5, 1, 10, 6, 9, 4, 7]
    print(bubble_sort(data))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())