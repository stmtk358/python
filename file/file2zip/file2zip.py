#! Python3
# 機能
#  特定のファイルをアーカイブする
# 使い方
#  1.Pythonを実行する
# 実行コマンド
#  python file2zip.py キーワード 検索パス
#  python file2zip.py .txt input
#  python file2zip.py テスト input

import os
import sys
import zipfile
import datetime

if len(sys.argv) != 3:
    sys.exit("使い方：python file2zip.py キーワード 検索パス")

keyword = sys.argv[1]
search_path = sys.argv[2]

# ファイル名：検索パス_システム日付(yyyymmdd).zip
sysdate = datetime.date.today().strftime("%Y%m%d")
zip_file_name = "{}_{}.zip".format(os.path.basename(search_path), sysdate)
print("Creating {}...".format(zip_file_name))

with zipfile.ZipFile(zip_file_name, "w") as zip_file:
    for folder_name, _, file_names in os.walk(search_path):
        # フォルダを追加する
        print("Adding files in {}...".format(folder_name))
        zip_file.write(folder_name)

        for file_name in file_names:
            # キーワードが含まれないファイルは対象外
            if keyword.lower() not in file_name.lower():
                continue

            # ファイルを追加する
            print("Adding file {}...".format(file_name))
            zip_file.write(os.path.join(folder_name, file_name))
