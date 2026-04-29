import asyncio
import micropip
from pyodide.http import pyfetch

async def main():
    # 外部ライブラリのインストール
    await micropip.install('pandas')
    
    import pandas as pd
    s1 = pd.Series([0, 1, 2])
    print(s1)

# メインスレッドを停止させないよう非同期で実行
if __name__ == '__main__':
    asyncio.ensure_future(main())