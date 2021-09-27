#! Python3
# 機能
#  巨大なファイルを探す
# 使い方
#  1.Pythonを実行する
# 実行コマンド
#  python huge_file_finder.py パス ファイルサイズ
#  python huge_file_finder.py C:\work\python 1000000

import os
import sys

if len(sys.argv) != 3:
    sys.exit("使い方：python huge_file_finder.py パス ファイルサイズ")

path = sys.argv[1]
search_size = int(sys.argv[2])
found = False

# サブフォルダも含めて検索する
for folder_name, _, file_names in os.walk(path):
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)

        # ファイルサイズを取得する
        try:
            file_size = os.path.getsize(file_path)
        except FileNotFoundError:
            print("size:不明 file:" + file_path)
            continue

        # 指定サイズ以上のファイルを出力する
        if file_size >= search_size:
            print("size:" + "{:,}".format(file_size) + " file:" + file_path)
            found = True

if not found:
    print("Not Found.")
