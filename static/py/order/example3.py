import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def g(cnt, n):
        for _ in range(n):
            cnt += 1
        return cnt

    def f(n):
        cnt = 0
        for _ in range(n):
            cnt = g(cnt, n)
        return cnt

    print(f(100))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())