import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def count_neighbors(board, i, j):
        cnt = 0
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                cnt += board[k][l]
        return cnt - board[i][j]


    board = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]
    print(count_neighbors(board, 1, 1))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())