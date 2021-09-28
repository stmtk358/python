#! Python3
# 機能
#  クリップボードのテキストを保存・復元・削除する
# 使い方
#  1.Pythonを実行する
# 実行コマンド
#  python multi_clipboard.py save キーワード
#  python multi_clipboard.py キーワード
#  python multi_clipboard.py list
#  python multi_clipboard.py delete キーワード

import os
import sys
import shelve
import pyperclip

os.makedirs("shelf", exist_ok=True)
with shelve.open("shelf/mcb") as shelf:
    if len(sys.argv) == 2:
        # 一覧
        if sys.argv[1].lower() == "list":
            pyperclip.copy(str(list(shelf.keys())))
            sys.exit()
        # 復元
        elif sys.argv[1] in shelf:
            pyperclip.copy(shelf[sys.argv[1]])
            sys.exit()
    elif len(sys.argv) == 3:
        # 保存
        if sys.argv[1].lower() == "save":
            shelf[sys.argv[2]] = pyperclip.paste()
            sys.exit()
        # 削除
        elif sys.argv[1].lower() == "delete":
            del shelf[sys.argv[2]]
            sys.exit()

print(
    """使い方：
python multi_clipboard.py save キーワード
python multi_clipboard.py キーワード
python multi_clipboard.py list
python multi_clipboard.py delete キーワード
"""
)
