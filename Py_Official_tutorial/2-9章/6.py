https://docs.python.org/ja/3/tutorial/modules.html


Python では定義をファイルに書いておき、スクリプトの中やインタプリタの対話インスタンス上で使う方法があります。このファイルを モジュール (module) と呼びます。

モジュールは Python の定義や文が入ったファイルです。ファイル名はモジュール名に接尾語 .py がついたものになります。モジュールの中では、(文字列の) モジュール名をグローバル変数 __name__ で取得できます。例えば、現在のディレクトリに以下の内容のファイル fibo.py を作成してみましょう:


次に Python インタプリタに入り、モジュールを以下のコマンドで import しましょう:

>>>
>>> import fibo
この操作では、fibo で定義された関数の名前を直接現在のシンボルテーブルに入力することはありません。単にモジュール名 fibo だけをシンボルテーブルに入れます。関数にはモジュール名を使ってアクセスします:

>>>
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
関数を度々使うのなら、ローカルな名前に代入できます:

>>>
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

各々のモジュールは、自分のプライベートなシンボルテーブルを持っていて、モジュールで定義されている関数はこのテーブルをグローバルなシンボルテーブルとして使います。したがって、モジュールの作者は、ユーザのグローバル変数と偶然的な衝突が起こる心配をせずに、グローバルな変数をモジュールで使うことができます。一方、自分が行っている操作をきちんと理解していれば、モジュール内の関数を参照するのと同じ表記法 modname.itemname で、モジュールのグローバル変数をいじることもできます。

モジュールが他のモジュールを import することもできます。 import 文は全てモジュールの(さらに言えばスクリプトでも)先頭に置きますが、これは慣習であって必須ではありません。 import されたモジュール名は import を行っているモジュールのグローバルなシンボルテーブルに置かれます。


import 文には、あるモジュール内の名前を、import を実行しているモジュールのシンボルテーブル内に直接取り込むという変型があります。例えば:

>>>
from fibo import fib, fib2
fib(500)

この操作は、import の対象となるモジュール名をローカルなシンボルテーブル内に取り入れることはありません (従って上の例では、 fibo は定義されません)。

モジュールで定義されている名前を全て import するという変型もあります:

>>>
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
この書き方では
アンダースコア (_) で始まるものを除いてすべての名前をインポートします。
殆どの場面で、Python プログラマーはこの書き方を使いません。未知の名前がインタープリターに読み込まれ、定義済みの名前を上書きしてしまう可能性があるからです。この操作を行うとしばしば可読性に乏しいコードになる

モジュール名の後に as が続いていた場合は、 as の後ろの名前を直接、インポートされたモジュールが束縛します。

>>>
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
これは実質的には import fibo と同じ方法でモジュールをインポートしていて、唯一の違いはインポートしたモジュールが fib という名前で取り扱えるようになっていることです。

このインポート方法は from が付いていても使え、同じ効果が得られます:

>>>
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
注釈 実行効率上の理由で、各モジュールはインタープリタの 1 セッションごとに 1 回だけ import されます。従って、モジュールを修正した場合には、インタープリタを再起動させなければなりません -- もしくは、その場で手直ししてテストしたいモジュールが 1 つだった場合には、例えば import importlib; importlib.reload(modulename) のように importlib.reload() を使ってください。

https://note.nkmk.me/python-if-name-main/
__name__とは
モジュールをインポートするとその__name__属性にモジュールの名前が文字列として格納される。<モジュール名>.__name__で取得できる。

import math
import numpy as np

print(math.__name__)
# math

print(np.__name__)
# numpy

他のファイルからインポートされた場合は__name__に'<モジュール名>'が格納され、コマンドラインからpython（またはpython3）コマンドで実行された場合は__name__に'__main__'という文字列が格納される。



sys.path
モジュールを検索するパスを示す文字列のリスト。 PYTHONPATH 環境変数と、インストール時に指定したデフォルトパスで初期化されます。

6.1.2. モジュール検索パス
spam という名前のモジュールをインポートするとき、インタープリターはまずその名前のビルトインモジュールを探します。見つからなかった場合は、 spam.py という名前のファイルを sys.path にあるディレクトリのリストから探します。 sys.path は以下の場所に初期化されます:

入力されたスクリプトのあるディレクトリ (あるいはファイルが指定されなかったときはカレントディレクトリ)。

PYTHONPATH (ディレクトリ名のリスト。シェル変数の PATH と同じ構文)。

インストールごとのデフォルト。

注釈 シンボリックリンクをサポートするファイルシステム上では、入力されたスクリプトのあるディレクトリはシンボリックリンクをたどった後に計算されます。言い換えるとシンボリックリンクを含むディレクトリはモジュール検索パスに追加 されません。
初期化された後、 Python プログラムは sys.path を修正することができます。スクリプトファイルを含むディレクトリが検索パスの先頭、標準ライブラリパスよりも前に追加されます。なので、ライブラリのディレクトリにあるファイルよりも、そのディレクトリにある同じ名前のスクリプトが優先してインポートされます。これは、標準ライブラリを意図して置き換えているのでない限りは間違いのもとです。より詳しい情報は 標準モジュール を参照してください。


import sys
print(sys.path)

['', 'C:\\local\\python38.zip', 'C:\\local\\DLLs', 'C:\\local\\lib', 'C:\\local', 'C:\\local\\lib\\site-packages', 'C:\\local\\lib\\site-packages\\win32', 'C:\\local\\lib\\site-packages\\win32\\lib', 'C:\\local\\lib\\site-packages\\Pythonwin']


6.2. 標準モジュール¶
変数 sys.path は文字列からなるリストで、インタプリタがモジュールを検索するときのパスを決定します。 sys.path は環境変数 PYTHONPATH から得たデフォルトパスに、 PYTHONPATH が設定されていなければ組み込みのデフォルト値に設定されます。標準的なリスト操作で変更することができます:

>>>
>>> import sys
# >>> sys.path.append('/ufs/guido/lib/python')

6.3. dir() 関数
組込み関数 dir() は、あるモジュールがどんな名前を定義しているか調べるために使われます。 dir() はソートされた文字列のリストを返します:

>>>
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
引数がなければ、 dir() は現在定義している名前を列挙します:

>>>
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
変数、モジュール、関数、その他の、すべての種類の名前をリストすることに注意してください。


dir() は、組込みの関数や変数の名前はリストしません。これらの名前からなるリストが必要なら、標準モジュール builtins で定義されています:

>>>
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']


 6.4. パッケージ¶


パッケージ (package) は、Python のモジュール名前空間を "ドット付きモジュール名" を使って構造化する手段です。例えば、モジュール名 A.B は、 A というパッケージのサブモジュール B を表します。ちょうど、モジュールを利用すると、別々のモジュールの著者が互いのグローバル変数名について心配しなくても済むようになるのと同じように、ドット付きモジュール名を利用すると、 NumPy や Pillow のように複数モジュールからなるパッケージの著者が、互いのモジュール名について心配しなくても済むようになります。

パッケージを import する際、 Python は sys.path 上のディレクトリを検索して、トップレベルのパッケージの入ったサブディレクトリを探します。
>>> sys.path
['', 'C:\\Anaconda3\\python38.zip', 'C:\\Anaconda3\\DLLs', 'C:\\Anaconda3\\lib', 'C:\\Anaconda3', 'C:\\Anaconda3\\lib\\site-packages', 'C:\\Anaconda3\\lib\\site-packages\\win32', 'C:\\Anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\Anaconda3\\lib\\site-packages\\Pythonwin']


ファイルを含むディレクトリをパッケージとしてPython に扱わせるには、ファイル __init__.py が必要です。 これにより、 string のようなよくある名前のディレクトリにより、モジュール検索パスの後の方で見つかる正しいモジュールが意図せず隠蔽されてしまうのを防ぐためです。 最も簡単なケースでは __init__.py はただの空ファイルで構いませんが、 __init__.py ではパッケージのための初期化コードを実行したり、後述の __all__ 変数を設定してもかまいません

パッケージのユーザは、個々のモジュールをパッケージから import することができます。例えば:

import sound.effects.echo
この操作はサブモジュール sound.effects.echo をロードします。このモジュールは、以下のように完全な名前で参照しなければなりません。

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
サブモジュールを import するもう一つの方法を示します:

from sound.effects import echo
これもサブモジュール echo をロードし、 echo をパッケージ名を表す接頭辞なしで利用できるようにします。従って以下のように用いることができます:

echo.echofilter(input, output, delay=0.7, atten=4)
さらにもう一つのバリエーションとして、必要な関数や変数を直接 import する方法があります:

from sound.effects.echo import echofilter
この操作も同様にサブモジュール echo をロードしますが、 echofilter() を直接利用できるようにします:

echofilter(input, output, delay=0.7, atten=4)

from package import item を使う場合、 item はパッケージ package のサブモジュール (またはサブパッケージ) でもかまいませんし、関数やクラス、変数のような、 package で定義されている別の名前でもかまわないことに注意してください。 import 文はまず、 item がパッケージ内で定義されているかどうか調べます。定義されていなければ、 item はモジュール名であると仮定して、モジュールをロードしようと試みます。もしモジュールが見つからなければ、 ImportError が送出されます。

反対に、 import item.subitem.subsubitem のような構文を使った場合、最後の subsubitem を除く各要素はパッケージでなければなりません。最後の要素はモジュールかパッケージにできますが、一つ前の要素で定義されているクラスや関数や変数にはできません。

sys.__path__