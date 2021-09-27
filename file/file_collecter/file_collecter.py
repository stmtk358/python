#! Python3
# 機能
#  特定のファイルを収集する
# 使い方
#  1.Pythonを実行する
# 実行コマンド
#  python file_collecter.py キーワード 検索パス 出力パス
#  python file_collecter.py .txt input output
#  python file_collecter.py テスト input output

import os
import sys
import shutil

if len(sys.argv) != 4:
    sys.exit("使い方：python file_collecter.py キーワード 検索パス 出力パス")

keyword = sys.argv[1]
search_path = sys.argv[2]
output_path = sys.argv[3]

# 出力フォルダを作成する
os.makedirs(output_path, exist_ok=True)

# サブフォルダも含めて検索する
for folder_name, _, file_names in os.walk(search_path):
    for file_name in file_names:
        # キーワードが含まれないファイルは対象外
        if keyword.lower() not in file_name.lower():
            continue

        # 対象ファイルをコピーする
        file_path = os.path.join(folder_name, file_name)
        print("Copying {}...".format(file_path))
        shutil.copy(file_path, output_path)
