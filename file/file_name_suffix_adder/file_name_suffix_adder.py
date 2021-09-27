#! Python3
# 機能
#  ファイル名にサフィックスを追加する
# 使い方
#  1.Pythonを実行する
# 実行コマンド
#  python file_name_suffix_adder.py パス
#  python file_name_suffix_adder.py input

import os
import sys
import shutil
import datetime

if len(sys.argv) != 2:
    sys.exit("使い方：python file_name_suffix_adder.py パス")
path = sys.argv[1]

# システム日付(yyyymmdd)をサフィックスにする
suffix = datetime.date.today().strftime("%Y%m%d")

for file_name in os.listdir(path):
    # 新ファイル名：ファイル名_サフィックス.拡張子
    base_name, extension = os.path.splitext(file_name)
    new_file_name = base_name + "_" + suffix + extension

    # リネームする
    file_path = os.path.join(path, file_name)
    new_file_path = os.path.join(path, new_file_name)
    print('Renaming "{}" to "{}"...'.format(file_path, new_file_path))
    shutil.move(file_path, new_file_path)
