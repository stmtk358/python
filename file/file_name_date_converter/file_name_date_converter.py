#! Python3
# 機能
#  ファイル名の日付をアメリカ式から日本式に変換する
# 使い方
#  1.Pythonを実行する
# 実行コマンド
#  python file_name_date_converter.py パス

import os
import re
import sys
import shutil

# アメリカ式日付の正規表現
date_pattern = re.compile(
    r"""
    ^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """,
    re.VERBOSE,
)

# ファイル名を変換する
def convert_file_name(file_name):
    # アメリカ式日付を含むファイル名を検索する
    match_object = date_pattern.search(file_name)
    if match_object == None:
        return None

    # ファイル名を分割する
    before_part = match_object.group(1)
    month = match_object.group(2)
    day = match_object.group(4)
    year = match_object.group(6)
    after_part = match_object.group(8)

    # 日本式日付のファイル名に変換する
    return before_part + year + "-" + month + "-" + day + after_part


if len(sys.argv) != 2:
    sys.exit("python file_name_date_converter.py パス")
path = sys.argv[1]

for file_name in os.listdir(path):
    # ファイル名を変換する
    new_file_name = convert_file_name(file_name)
    if new_file_name == None:
        continue

    # リネームする
    file_path = os.path.join(path, file_name)
    new_file_path = os.path.join(path, new_file_name)
    print('Renaming "{}" to "{}"...'.format(file_path, new_file_path))
    shutil.move(file_path, new_file_path)
