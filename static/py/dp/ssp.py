import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def ssp(a, N):
        # 初期化
        dp = [[False for _ in range(N + 1)] for _ in range(len(a) + 1)]
        for i in range(len(a) + 1):
            dp[i][0] = True
        # DP
        for i in range(1, len(a) + 1):
            for j in range(N + 1):
                if a[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - a[i - 1]]
        return dp[len(a)][N]

    print(ssp([3, 4, 6], 10))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())