import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def evaluate_grade(point):
        if point >= 90:
            print("優上です。非常に素晴らしい成績です。")
        elif point >= 80:
            print("優です。素晴らしい成績です。")
        elif point >= 65:
            print("良です。よく理解できています。")
        elif point >= 50:
            print("可です。よく勉強しています。")
        else:
            print("不可です。もう少し頑張りましょう。")

    evaluate_grade(79)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())