import os #列出資料夾的檔名

import pandas as pd #讀excel

Path = input('輸入資料夾路徑:')
a = input('輸入關鍵字:')


allFile = os.listdir(Path) #回傳資料夾中的所有檔名

for f in allFile:
    pd.set_option("display.max_columns", None) #展開欄
    pd.set_option("display.max_rows", None) #展開列
    df = pd.read_excel(f, sheet_name = None)#不限定分頁
    ans = str(df)
    if a in ans:
        print(f)
