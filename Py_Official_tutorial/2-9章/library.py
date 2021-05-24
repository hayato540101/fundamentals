10.2. ファイルのワイルドカード表記
glob モジュールでは、ディレクトリのワイルドカード検索からファイルのリストを生成するための関数を提供しています:

>>>
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']