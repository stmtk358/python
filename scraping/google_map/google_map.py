#! python3
# 機能
#  コマンドラインで指定した住所をGoogleマップで開く
# 使い方
#  1.Pythonを実行する
# 実行コマンド
#  python google_map.py 住所
#  python google_map.py 東京
#  python google_map.py 東京 新宿

import sys
import webbrowser

if len(sys.argv) < 2:
    sys.exit("使い方：python google_map.py 住所")

address = " ".join(sys.argv[1:])
webbrowser.open("https://www.google.com/maps/search/" + address)
