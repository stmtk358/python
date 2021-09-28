#! Python3
# 機能
#  ファイルの文字コードを変換する
# 使い方
#  1.Pythonを実行する
# 実行コマンド
#  python file_encoder.py パス 入力文字コード 出力文字コード
#  python file_encoder.py input shift_jis utf-8

import os
import sys
import codecs

if len(sys.argv) != 4:
    sys.exit("使い方：python file_encoder.py パス 入力文字コード 出力文字コード")

path = sys.argv[1]
enc_from = sys.argv[2]
enc_to = sys.argv[3]

for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)
    print("Encoding {}...".format(file_path))

    # 入力文字コードでファイルを読み込む
    with codecs.open(file_path, "r", enc_from) as file:
        row_data = []
        for row in file:
            row_data.append(row)

    # 出力文字コードでファイルに書き込む
    with codecs.open(file_path, "w", enc_to) as file:
        for row in row_data:
            file.write(row)
