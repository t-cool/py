import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def gauss_jordan_elimination(a):
        # 前進消去
        for i in range(len(a)):
            # 部分ピボット選択
            max_index = i
            for j in range(i + 1, len(a)):
                if abs(a[max_index][i]) < abs(a[j][i]):
                    max_index = j
                    a[i], a[max_index] = a[max_index], a[i]

            # pivot倍で行を割る
            pivot = a[i][i]
            for j in range(i, len(a[i])):
                a[i][j] /= pivot

            # highlight-start
            # 掃き出す
            for j in range(len(a)):
                if j != i:
                    factor = a[j][i]
                    for k in range(i, len(a[i])):
                        a[j][k] -= factor * a[i][k]
            # highlight-end
        # highlight-start
        x = []
        for i in range(len(a)):
            x.append(a[i][len(a[i]) - 1])
        return x
        # highlight-end

    print(gauss_jordan_elimination([[0, -2, 3, 2], [-1, 3, -2, 1], [1, -1, 6, 11]]))

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())