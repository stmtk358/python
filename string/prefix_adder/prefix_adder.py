#! Python3
# 機能
#  テキストの各行にプレフィックスを追加する
# 使い方
#  1.テキストをコピーする
#  2.Pythonを実行する
#  3.実行結果がコピーされる
# 実行コマンド
#  python prefix_adder.py
#  python prefix_adder.py #
#  python prefix_adder.py "# "

import sys
import pyperclip

# プレフィックスを設定する（引数優先）
prefix = "* "
if len(sys.argv) == 2:
    prefix = sys.argv[1]

# コピーされたテキストを取得し、行ごとに分割する
text = pyperclip.paste()
lines = text.split("\n")

# 行ごとにプレフィックスを追加する
for i in range(len(lines)):
    lines[i] = prefix + lines[i]

# 行を連結して、コピーする
output = "\n".join(lines)
pyperclip.copy(output)
