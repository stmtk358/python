#! Python3
# 機能
#  CSVファイルからフォルダを作成する
# 使い方
#  1.CSVファイルを配置する
#  2.Pythonを実行する
# 実行コマンド
#  python folder_maker.py CSVパス 出力パス

import os
import sys
import csv

if len(sys.argv) != 3:
    sys.exit("python folder_maker.py CSVパス 出力パス")

csv_path = sys.argv[1]
output_path = sys.argv[2]

# CSVファイルを読み込む
with open(csv_path, encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    # CSVデータをアンダーバー区切りにしたフォルダを作成する
    for row in csv_reader:
        folder_name = "_".join(row)
        folder_path = os.path.join(output_path, folder_name)
        print('Making "{}"...'.format(folder_path))
        os.makedirs(folder_path, exist_ok=True)

