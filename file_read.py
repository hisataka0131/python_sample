#ファイル読み込み

open_file = open('point.txt')
raw_data = open_file.read()
open_file.close()
print(raw_data)