import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def knapsack(v, w, W):
        # 初期化
        dp = [[0 for _ in range(W + 1)] for _ in range(len(v) + 1)]
        # DP
        for i in range(1, len(v) + 1):
            for j in range(W + 1):
                if w[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
        return dp[len(v)][W]

    print(knapsack([2, 3, 6], [2, 3, 5], 10))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())