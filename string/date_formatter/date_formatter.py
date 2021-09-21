#! Python3
# 機能
#  日付の表記ゆれを統一する
#  変換対象：YYYY/M/D, YYYY/MM/DD, YYYY-M-D, YYYY-MM-DD, YYYY年M月D日, YYYY年MM月DD日
#  変換後：YYYY/MM/DD
# 使い方
#  1.テキストをコピーする
#  2.Pythonを実行する
#  3.実行結果がコピーされる
# 実行コマンド
#  python date_formatter.py

import re
import pyperclip

# テキストを取得する
text = pyperclip.paste()

# スラッシュ区切りに変換する
regex = re.compile(r"((19|20)\d\d)[-/年]((0|1)?\d)[-/月]((0|1|2|3)?\d)日?")
output = regex.sub(r"\1/\3/\5", text)

# ゼロ埋めする
regex = re.compile(r"((19|20)\d\d)/(\d)/(\d)")
output = regex.sub(r"\1/0\3/0\4", output)

# テキストをコピーする
pyperclip.copy(output)
