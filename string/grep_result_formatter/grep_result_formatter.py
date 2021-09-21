#! Python3
# 機能
#  サクラエディタのGrep結果をExcel用に整形する
# 使い方
#  1.テキストをコピーする
#  2.Pythonを実行する
#  3.実行結果がコピーされる
# 実行コマンド
#  python grep_result_formatter.py

import re
import pyperclip

# テキストを取得する
text = pyperclip.paste()

# Grep結果をタブ区切りに変換する
regex = re.compile(r"(^.*?)\((.*),(.*)\)\s+\[(.*)\]:(\s+)", re.MULTILINE)
output = regex.sub(r"\1\t\2\t\3\t\4\t", text)

# テキストをコピーする
pyperclip.copy(output)
