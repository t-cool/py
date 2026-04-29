import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def merge(left, right):
        if len(left) == 0 or len(right) == 0:
            return left + right
        # highlight-next-line
        if left[0] > right[0]:
            return [left[0]] + merge(left[1:], right)
        else:
            return [right[0]] + merge(left, right[1:])


    def merge_sort(data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = merge_sort(data[:mid])
        right = merge_sort(data[mid:])
        return merge(left, right)


    data = [3, 8, 2, 5, 1, 10, 6, 9, 4, 7]
    print(merge_sort(data))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())