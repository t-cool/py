import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    age = 18
    if age < 18:
        print("選挙権はありません。")
    elif age < 25:
        print("投票することができます。")
    else:
        print("衆議院議員に立候補することができます。")

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())