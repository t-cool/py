import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def gaussian_elimination_revised(a):
        # 前進消去
        for i in range(len(a)):
            # highlight-start
            # 部分ピボット選択
            max_index = i
            for j in range(i + 1, len(a)):
                if abs(a[max_index][i]) < abs(a[j][i]):
                    max_index = j
            a[i], a[max_index] = a[max_index], a[i]
            # highlight-end

            # pivot倍で行を割る
            pivot = a[i][i]
            for j in range(i, len(a[i])):
                a[i][j] /= pivot

            # i + 1行目以降を掃き出す
            for j in range(i + 1, len(a)):
                factor = a[j][i]
                for k in range(i, len(a[i])):
                    a[j][k] -= factor * a[i][k]

        # 後退代入
        x = [0 for _ in range(len(a[0]) - 1)]
        for i in reversed(range(len(a))):
            x[i] = a[i][len(a[i]) - 1]
            for j in range(i):
                a[j][len(a[i]) - 1] -= a[j][i] * x[i]
        return x


    print(gaussian_elimination_revised([[0, -2, 3, 2], [-1, 3, -2, 1], [1, -1, 6, 11]]))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())