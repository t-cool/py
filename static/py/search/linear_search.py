import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def linear_search(data, name):
        for i in range(len(data)):
            if data[i] == name:
                return i


    students = [
        "伊藤",
        "井上",
        "加藤",
        "木村",
        "小林",
        "斎藤",
        "佐々木",
        "佐藤",
        "清水",
        "鈴木",
        "高橋",
        "田中",
        "中村",
        "林",
        "松本",
        "山田",
        "山口",
        "山本",
        "吉田",
        "渡辺",
    ]

    print(linear_search(students, "佐藤") + 1)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())