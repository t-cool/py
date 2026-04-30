import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    pass
    
    def introduce_self(name, language):
        print("私の名前は、" + name + "です。" + language + "選択です。")

    introduce_self("東大太郎", "中国語")

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())