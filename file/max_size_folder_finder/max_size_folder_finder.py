#! Python3
# 機能
#  最もディスク容量を使用しているフォルダを探す
# 使い方
#  1.Pythonを実行する
# 実行コマンド
#  python max_size_folder_finder.py パス
#  python max_size_folder_finder.py C:\work\python

import os
import sys

if len(sys.argv) != 2:
    sys.exit("使い方：python max_size_folder_finder.py パス")

path = sys.argv[1]
max_size = 0
max_size_folder = ""

# サブフォルダも含めて検索する
for folder_name, _, file_names in os.walk(path):

    total_size = 0
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)

        # ファイルサイズを取得する
        try:
            total_size += os.path.getsize(file_path)
        except:
            print("size:不明 file:" + file_path)

    # 合計サイズが上回ったらサイズとフォルダ名を更新する
    if total_size > max_size:
        max_size = total_size
        max_size_folder = folder_name

print("サイズ：" + "{:,}".format(max_size))
print("フォルダ：" + max_size_folder)
