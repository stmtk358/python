#! Python3
# 機能
#  テキストの各行に連番を追加する
# 使い方
#  1.テキストをコピーする
#  2.Pythonを実行する
#  3.実行結果がコピーされる
# 実行コマンド
#  python number_adder.py

import pyperclip

# テキストを取得し、行ごとに分割する
text = pyperclip.paste()
lines = text.split("\n")

# 連番を追加する
for i in range(len(lines)):
    lines[i] = "{}.{}".format((i + 1), lines[i])

# 行を連結し、コピーする
output = "\n".join(lines)
pyperclip.copy(output)
