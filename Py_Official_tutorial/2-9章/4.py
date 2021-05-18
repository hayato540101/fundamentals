4.2. for 文
Python の for 文は、任意のシーケンス型 (リストまたは文字列) にわたって反復を行います。反復の順番はシーケンス中に要素が現れる順番です。

コレクションオブジェクト(おそらく要素を複数所持しているオブジェクト)
の値を反復処理をしているときに、そのコレクションオブジェクトを変更するコードは理解するのが面倒になり得ます。 そうするよりも、コレクションオブジェクトのコピーに対して反復処理をするか、新しいコレクションオブジェクトを作成する方が通常は理解しやすいです:

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

4.3. range() 関数
# 数列にわたって反復を行う必要がある場合、組み込み関数 range() が便利です。この関数は算術型の数列を生成します:

>>>
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
指定した終端値は生成されるシーケンスには入りません。←rangeはシーケンスを生成している。
range(10) は 10 個の値を生成し、長さ 10 のシーケンスにおける各項目のインデクスとなります。range を別の数から開始したり、他の増加量 (負でも; 増加量は時に 'ステップ(step)' と呼ばれることもあります) を指定することもできます:

あるシーケンスにわたってインデクスで反復を行うには、 range() と len() を次のように組み合わせられます:

>>>
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
しかし、多くの場合は enumerate() 関数を使う方が便利です。 ループのテクニック を参照してください。

range を直接出力すると変なことになります:

>>>
>>> print(range(10))
range(0, 10)
range() が返すオブジェクトは、いろいろな点でリストであるかのように振る舞いますが、本当はリストではありません。これは、'''イテレートした時に望んだ数列の連続した要素を返すオブジェクトです。しかし実際にリストを作るわけではないので、スペースの節約になります。'''

このようなオブジェクトは イテラブル (iterable) と呼ばれます。 '''これらは関数や構成物のターゲットとして、あるだけの項目を逐次与えるのに適しています。''' 
for 文がそのような構成物であることはすでに見てきており、イテラブルを受け取る関数の例には sum() があります:

>>>
>>> sum(range(4))  # 0 + 1 + 2 + 3
6
後ほど、イテラブルを返したりイテラブルを引数として取る関数をもっと見ていきます。 そして最後に、どうやって range からリストを作るのかが気になるかもしれません。 これが答えです:

>>>
>>> list(range(4))
[0, 1, 2, 3]
データ構造 の章では、 list() についてより詳細に議論します。


pass のもう 1 つの使い道は、新しいコードを書いているときの関数や条件文の仮置きの本体としてです。こうすることで、より抽象的なレベルで考え続けられます。 pass は何事も無く無視されます

>>>
>>> def initlog(*args):
...     pass   # Remember to implement this!


4.6. 関数を定義する


# フィボナッチ数列の数からなるリストを出力する代わりに、値を返すような関数を書くのは簡単です:

>>> def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
この例は Python の新しい機能を示しています:

return 文では、関数から一つ値を返します。 return の引数となる式がない場合、 None が返ります。関数が終了したときにも None が返ります。

文 result.append(a) では、リストオブジェクト result の メソッド (method) を呼び出しています。
メソッドとは、オブジェクトに '属している' 関数のことで、 obj を何らかのオブジェクト (式であっても構いません)、 methodname をそのオブジェクトで定義されているメソッド名とすると、 obj.methodname と書き表されます。

異なる型は異なるメソッドを定義しています。異なる型のメソッドで同じ名前のメソッドを持つことができ、あいまいさを生じることはありません。 (クラス (class) を使うことで、自前のオブジェクト型とメソッドを定義することもできます。 
クラス 参照) 例で示されているメソッド append() は、リストオブジェクトで定義されています; 
このメソッドはリストの末尾に新たな要素を追加します。この例での append() は result = result + [a] と等価ですが、より効率的です。


デフォルト値は、関数が定義された時点で、関数を 定義している 側のスコープ (scope) で評価されるので

i = 5

def f(arg=i):
    print(arg)

i = 6
f()
は 5 を出力します。

'''重要な警告: デフォルト値は 1 度だけしか評価されません。'''
デフォルト値がリストや辞書のような変更可能なオブジェクトの時にはその影響がでます。例えば以下の関数は、後に続く関数呼び出しで関数に渡されている引数を累積します:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
このコードは、以下を出力します

[1]
[1, 2]
[1, 2, 3]
後続の関数呼び出しでデフォルト値を共有したくなければ、代わりに以下のように関数を書くことができます:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L



4.7.2. キーワード引数
関数を kwarg=value という形式の キーワード引数 を使って呼び出すこともできます。例えば、以下の関数:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
は、必須引数 (voltage) とオプション引数 (state、action、type) を受け付けます。この関数は以下のいずれかの方法で呼び出せます:

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
が、以下の呼び出しは不適切です:

parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
関数の呼び出しにおいて、キーワード引数は位置引数の後でなければなりません。渡されるキーワード引数は全て、関数で受け付けられる引数のいずれかに対応していなければならず (例えば、actor はこの parrot 関数の引数として適切ではありません)、順序は重要ではありません。これはオプションでない引数でも同様です (例えば、parrot(voltage=1000) も適切です)。いかなる引数も値を複数回は受け取れません。この制限により失敗する例は:

>>>
>>> def function(a):
...     pass
...
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for keyword argument 'a'

'''仮引数の最後に **name の形式のもの ←キーワード付き引数のこと'''
があると、それまでの仮引数に対応したものを除くすべてのキーワード引数が入った辞書 (マッピング型 --- dict を参照) を受け取ります。 **name は *name の形式をとる、仮引数のリストを超えた位置引数の入った タプル を受け取る引数 (次の小節で述べます) と組み合わせられます。 (*name は **name より前になければなりません)。 例えば、ある関数の定義を以下のようにすると:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
呼び出しは以下のようになり:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
もちろん以下のように出力されます:

-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
なお、複数のキーワード引数を与えた場合に、それらが出力される順序は、関数呼び出しで与えられた順序と同じになります。


4.7.3. 特殊なパラメータ
デフォルトでは、引数は位置またはキーワードによる明示で Python 関数に渡されます。 可読性とパフォーマンスのために、その引数が位置、位置またはキーワード、キーワードのどれで渡されるかを開発者が判定するのに関数定義だけを見ればよいように、引数の渡され方を制限することには意味があります。

関数定義は次のようになります:

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
ここで、/ と * はオプションです。使用された場合、これらの記号は、引数が関数に渡される方法、すなわち、位置専用、位置またはキーワード、キーワード専用、といった引数の種類を示します。キーワード引数は、名前付き引数とも呼ばれます。

4.7.3.1. 位置またはキーワード引数
関数定義に / も * もない場合は、引数は位置またはキーワードで関数に渡されます。

4.7.3.2. 位置専用引数
これをもう少し詳しく見てみると、特定の引数を 位置専用 と印を付けられます。 位置専用 の場合、引数の順序が重要であり、キーワードで引数を渡せません。 位置専用引数は / （スラッシュ）の前に配置されます。 / は、位置専用引数を残りの引数から論理的に分離するために使用されます。 関数定義に / がない場合、位置専用引数はありません。

/ の後の引数は、 位置またはキーワード 、もしくは、 キーワード専用 です。

4.7.3.3. キーワード専用引数
引数をキーワード引数で渡す必要があることを示す キーワード専用 として引数をマークするには、引数リストの最初の キーワード専用 引数の直前に * を配置します。'''キーワード専用引数は*の後に書かれることに注意'''


4.7.3.4. 関数の例
/ および * といったマーカーに注意を払って、次の関数定義の例を見てください:

>>> def standard_arg(arg):
...     print(arg)
...
>>> def pos_only_arg(arg, /):
...     print(arg)
...
>>> def kwd_only_arg(*, arg):
...     print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)
最も馴染みのある形式の最初の関数定義 standard_arg は、呼び出し規約に制限を設けておらず、引数は位置またはキーワードで渡されます:

>>>
>>> standard_arg(2)
2

>>> standard_arg(arg=2)
2

2番目の関数の pos_only_arg は、 / が関数定義にあるので、引数は位置専用になります:
>>> pos_only_arg(1)
1

>>> pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got an unexpected keyword argument 'arg'


3番目の関数 kwd_only_args は、関数定義に * があるので、引数はキーワード専用になります:
>>> kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

>>> kwd_only_arg(arg=3)
3
そして最後の関数は3つの引数の種類を一つの関数定義の中で使用しています:

>>>
>>> combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given

>>> combined_example(1, 2, kwd_only=3)
1 2 3

>>> combined_example(1, standard=2, kwd_only=3)
1 2 3

>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got an unexpected keyword argument 'pos_only'


最後に、位置引数 name と name をキーとして持つ **kwds の間に潜在的な衝突がある関数定義を考えてみましょう。

def foo(name, **kwds):
    return 'name' in kwds
キーワードに 'name' を入れても、先頭の引数と同じになってしまうため、この関数が True を返すような呼び出しの方法はありません。例えば、次のようになってしまいます:

>>>
>>> foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
>>>
しかし位置専用を示す / を使用すれば可能になります。 name は位置引数として、そして 'name' はキーワード引数のキーワードとして認識されるからです:

def foo(name, /, **kwds):
    return 'name' in kwds
>>> foo(1, **{'name': 2})
True
言い換えると、位置専用引数であれば、その名前を **kwds の中で使用しても、曖昧にならないということです。


ハッシュ化の話
https://www.agent-grow.com/self20percent/2018/11/19/what-is-hash/

hashable
(ハッシュ可能) ハッシュ可能 なオブジェクトとは、生存期間中変わらないハッシュ値を持ち (__hash__() メソッドが必要)、他のオブジェクトと比較ができる (__eq__() メソッドが必要) オブジェクトです。同値なハッシュ可能オブジェクトは必ず同じハッシュ値を持つ必要があります。

ハッシュ可能なオブジェクトは辞書のキーや集合のメンバーとして使えます。辞書や集合のデータ構造は内部でハッシュ値を使っているからです。

Python のイミュータブルな組み込みオブジェクトは、ほとんどがハッシュ可能です。(リストや辞書のような) ミュータブルなコンテナはハッシュ不可能です。(タプルや frozenset のような) イミュータブルなコンテナは、要素がハッシュ可能であるときのみハッシュ可能です。 ユーザー定義のクラスのインスタンスであるようなオブジェクトはデフォルトでハッシュ可能です。 それらは全て (自身を除いて) 比較結果は非等価であり、ハッシュ値は id() より得られます。


iterable
(反復可能オブジェクト) 要素を一度に 1 つずつ返せるオブジェクトです。 反復可能オブジェクトの例には、(list, str, tuple といった) 全てのシーケンス型や、 dict や ファイルオブジェクト といった幾つかの非シーケンス型、 あるいは Sequence 意味論を実装した __iter__() メソッドか __getitem__() メソッドを持つ任意のクラスのインスタンスが含まれます。

反復可能オブジェクトは for ループ内やその他多くのシーケンス (訳注: ここでのシーケンスとは、シーケンス型ではなくただの列という意味)が必要となる状況 (zip(), map(), ...) で利用できます。 反復可能オブジェクトを組み込み関数 iter() の引数として渡すと、 オブジェクトに対するイテレータを返します。 このイテレータは一連の値を引き渡す際に便利です。 通常は反復可能オブジェクトを使う際には、 iter() を呼んだりイテレータオブジェクトを自分で操作する必要はありません。 for 文ではこの操作を自動的に行い、一時的な無名の変数を作成してループを回している間イテレータを保持します。 イテレータ 、 シーケンス 、 ジェネレータ も参照してください。

iterator
(イテレータ) データの流れを表現するオブジェクトです。イテレータの __next__() メソッドを繰り返し呼び出す (または組み込み関数 next() に渡す) と、流れの中の要素を一つずつ返します。データがなくなると、代わりに StopIteration 例外を送出します。その時点で、イテレータオブジェクトは尽きており、それ以降は __next__() を何度呼んでも StopIteration を送出します。イテレータは、そのイテレータオブジェクト自体を返す __iter__() メソッドを実装しなければならないので、イテレータは他の iterable を受理するほとんどの場所で利用できます。はっきりとした例外は複数の反復を行うようなコードです。 (list のような) コンテナオブジェクトは、自身を iter() 関数にオブジェクトに渡したり for ループ内で使うたびに、新たな未使用のイテレータを生成します。これをイテレータで行おうとすると、前回のイテレーションで使用済みの同じイテレータオブジェクトを単純に返すため、空のコンテナのようになってしまします。

詳細な情報は イテレータ型 にあります。

(7) マッピング型
キーとなる値（key）を任意のオブジェクト（value）に対応付けるデータ型です。キーをインデックスとしてオブジェクトを検索するため、キーは他のキーと比較し区別できる必要があり、ミュータブルな値をキーにすることはできません。標準のマッピング型は辞書 (dict) だけです。

https://snowtree-injune.com/2019/12/04/word-container/#container-types
(8) コンテナ
コンテナとは「複数のオブジェクトを格納できるオブジェクト」です。数値型やboolは複数のオブジェクトを格納できないのでコンテナではありません。

Pythonのドキュメントでは、コンテナについて「他のオブジェクトに対する参照をもつオブジェクト」と紹介してされています。 他のオブジェクトに対する参照を集めてひとまとめにしています。

他のオブジェクトに対する参照をもつオブジェクトもあります; これらは コンテナ (container) と呼ばれます。コンテナオブジェクトの例として、タプル、リスト、および辞書が挙げられます。オブジェクトへの参照自体がコンテナの値の一部です。

Python ドキュメント >> Python 言語リファレンス >> 3. データモデル >> 3.1. オブジェクト、値、および型
シーケンス型、辞書型、集合型がコンテナであり、以下のデータ型がコンテナに分類されます。


イテレータ
https://python.ms/iterator/

イテレータとは、list, tuple, set などの集合を表現するオブジェクトを  iter 関数  を使って  コピー  したようなものです。

a = [1, 2, 3, 4]
b = iter(a)
b
list(b)
>>> b
<list_iterator object at 0x10d8458d0>
>>> list(b)
[1, 2, 3, 4]  # <--- イテレータは、コピーみたいなもの

イテレータからは   next 関数  を使って、 １つずつ要素を  取り出す  ことができます。

a = [1, 2, 3, 4]
b = iter(a)
next(b)
next(b)
next(b)
next(b)
next(b)
next(b)

for 文はイテレータを回していた(イテレータを回すためのiter()関数(イテレータを生成)とnext()関数(コンテナの次のアイテムを返します。もしそれ以上アイテムが無ければ StopIteration 例外を送出)をフックにしていた。)


class Team:
    def __init__(self):
        self._member_list = []

team = Team()
team._member_list.extend(
    ['川島 永嗣', '香川 真司', '長谷部 誠'])
'''末尾に別のリストやタプルを結合（連結）: extend(), +演算子
リストのメソッドextend()で、末尾（最後）に別のリストやタプルを結合できる。すべての要素が元のリストの末尾に追加される。
'''

>>> for member in team._member_list:  # <- 長い
...     print(member)
... 
川島 永嗣
香川 真司
長谷部 誠
>>> 
こんな風に in の中に自分が定義したクラスのオブジェクトが書けるようになります。

 次のコードを対話モードにコピペして実行してみてください。  対話モードというのは、あのトンガリマークが３つ連なった >>> 記号が表示される画面ことです。

#
# 対話モード >>> に
# コピペで実行できます。
#
class Team:
    def __init__(self):
        self._member_list = []
    
    def __iter__(self):  # <- これを付け足すだけ
        return iter(self._member_list) # イテレータを生成

team = Team()
team._member_list.extend(
    ['川島 永嗣', '香川 真司', '長谷部 誠'])

for member in team:  # <- 短い
    print(member)
おそらく、for文が実行される前に__iter__関数が実行される仕様になっている

上記のように for 文の in に書き込めるできるインスタンスオブジェクトまたはクラスを  イテラブル  と言います。 Team はイテラブルです。 イテラブルは、この先かなり頻繁に登場する単語です。


◯ 出来るようになること
その２ 集合を引数に取る関数で使えるようになる
set 関数を用いて差集合、和集合を取ったり、 max 関数を用いて集合の最大値を取ったりすることもできるようになったりもします。

こんな風に書いていたのを

#
# 対話モード >>> に
# コピペで実行できます。
#
class Team:
    def __init__(self):
        self._member_list = []

team_a = Team()
team_a._member_list.extend(
    ['川島 永嗣', '香川 真司', '長谷部 誠'])

team_b = Team()
team_b._member_list.extend(
    ['川島 永嗣', '香川 真司', '原口 元気'])

set(team_a._member_list) - set(team_b._member_list)
>>> set(team_a._member_list) - set(team_b._member_list) 
{'長谷部 誠'}
>>>
こんな風に書き換えたりもできたりします。  次のコードを対話モードにコピペして実行してみてください。 

#
# 対話モード >>> に
# コピペで実行できます。
#
class Team:
    def __init__(self):
        self._member_list = []
    
    def __iter__(self):  # <- これを付け足すだけ
        return iter(self._member_list)

team_a = Team()
team_a._member_list.extend(
    ['川島 永嗣', '香川 真司', '長谷部 誠'])

team_b = Team()
team_b._member_list.extend(
    ['川島 永嗣', '香川 真司', '原口 元気'])

set(team_a) - set(team_b)
>>> set(team_a) - set(team_b)  # <- 短くなりました。
{'長谷部 誠'}
>>>
他にもイテラブルを引数に取る関数が使えるようになります。 


for 文が実行されているとき

リスト = [1, 2, 3, 4]
for 要素 in リスト:
    print(要素)
内部ではこんな感じで呼び出されています。

リスト = [1, 2, 3, 4]
イテレータ = iter(リスト)
while True:
    try:
        要素 = next(イテレータ)
    except StopIteration:
        break
    print(要素)

→for文のフックはiter()関数とnext()関数



4.7.6. ラムダ式
キーワード lambda を使うと、名前のない小さな関数を生成できます。例えば lambda a, b: a+b は、二つの引数の和を返す関数です。ラムダ式の関数は、関数オブジェクトが要求されている場所にならどこでも使うことができます。ラムダ式は、構文上単一の式に制限されています。意味付け的には、ラムダ形式は単に通常の関数定義に構文的な糖衣をかぶせたものに過ぎません。入れ子構造になった関数定義と同様、ラムダ式もそれを取り囲むスコープから変数を参照することができます:

def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
f(0)
f(1)