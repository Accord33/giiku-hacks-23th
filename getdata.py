import csv
import re

# 入力ファイルと出力ファイルのパス
input_file = '/Users/sakabekazuto/prg/git/giiku-hacks/giiku-hacks2/database.csv'
output_file = '/Users/sakabekazuto/prg/git/giiku-hacks/giiku-hacks2/extracted_data.csv'

# 正規表現パターン
url_pattern = re.compile(r'src="([^"]+)"')
title_pattern = re.compile(r'title="([^"]+)"')

# 新しいCSVファイルのヘッダー
headers = ['URL', 'Title', 'Category']

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer.writerow(headers)
    
    for row in reader:
        iframe = row[0]
        category = row[1]
        
        # URLとタイトルを抽出
        url_match = url_pattern.search(iframe)
        title_match = title_pattern.search(iframe)
        
        if url_match and title_match:
            url = url_match.group(1)
            title = title_match.group(1)
            writer.writerow([url, title, category])