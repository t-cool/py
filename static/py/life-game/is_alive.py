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
                if 0 <= k < len(board) and 0 <= l < len(board[k]):
                    cnt += board[k][l]
        return cnt - board[i][j]


    # highlight-start
    def is_alive(board, i, j):
        neighbors_cnt = count_neighbors(board, i, j)
        if board[i][j] == 0:
            if neighbors_cnt == 3:
                return 1
            else:
                return 0
        else:
            if 2 <= neighbors_cnt <= 3:
                return 1
            elif neighbors_cnt <= 1:
                return 0
            elif neighbors_cnt >= 4:
                return 0


    # highlight-end


    board = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]
    print(is_alive(board, 0, 0))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())