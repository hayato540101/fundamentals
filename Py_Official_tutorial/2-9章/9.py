https://docs.python.org/ja/3/tutorial/classes.html

9.1. 名前とオブジェクトについて¶

オブジェクトには個体性があり、同一のオブジェクトに(複数のスコープから) 複数の名前を割り当てることができます。この機能は他の言語では別名づけ(alias) として知られています。 Python を一見しただけでは、別名づけの重要性は分からないことが多く、変更不能な基本型 (数値、文字列、タプル)を扱うときには無視して差し支えありません。しかしながら、別名付けは、リストや辞書や他の多くの型など、変更可能な型を扱う Python コード上で驚くべき効果があります。別名付けはいくつかの点でポインタのように振舞い、このことは通常はプログラムに利するように使われます。例えば、オブジェクトの受け渡しは、実装上はポインタが渡されるだけなのでコストの低い操作になります。また、関数があるオブジェクトを引数として渡されたとき、関数の呼び出し側からオブジェクトに対する変更を見ることができます --- これにより、 Pascal にあるような二つの引数渡し機構をもつ必要をなくしています。


9.2. Python のスコープと名前空間¶

名前空間 (namespace) とは、名前からオブジェクトへの対応付け (mapping) です。ほとんどの名前空間は、現状では Python の辞書として実装されていますが、そのことは通常は (パフォーマンス以外では) 目立つことはないし、将来は変更されるかもしれません。名前空間の例には、組込み名の集合 (abs() 等の関数や組込み例外名)、モジュール内のグローバルな名前、関数を呼び出したときのローカルな名前があります。オブジェクトの属性からなる集合もまた、ある意味では名前空間です。名前空間について知っておくべき重要なことは、異なった名前空間にある名前の間には全く関係がないということです。例えば、二つの別々のモジュールの両方で関数 maximize という関数を定義することができ、定義自体は混同されることはありません
 --- モジュールのユーザは名前の前にモジュール名をつけなければなりません。

ところで、 属性 という言葉は、ドットに続く名前すべてに対して使っています --- 例えば式 z.real で、 real はオブジェクト z の属性です。厳密にいえば、モジュール内の名前に対する参照は属性の参照です。式 modname.funcname では、 modname はあるモジュールオブジェクトで、 funcname はその属性です。この場合には、モジュールの属性とモジュールの中で定義されているグローバル名の間には、直接的な対応付けがされます。これらの名前は同じ名前空間を共有しているのです！ 1

属性は読取り専用にも、書込み可能にもできます。書込み可能であれば、属性に代入することができます。モジュール属性は書込み可能で、 modname.the_answer = 42 と書くことができます。書込み可能な属性は、 del 文で削除することもできます。例えば、 del modname.the_answer は、 modname で指定されたオブジェクトから属性 the_answer を除去します。

名前空間は様々な時点で作成され、その寿命も様々です。組み込みの名前が入った名前空間は Python インタプリタが起動するときに作成され、決して削除されることはありません。モジュールのグローバルな名前空間は、モジュール定義が読み込まれたときに作成されます。通常、モジュールの名前空間は、インタプリタが終了するまで残ります。インタプリタのトップレベルで実行された文は、スクリプトファイルから読み出されたものでも対話的に読み出されたものでも、 __main__ という名前のモジュールの一部分であるとみなされるので、独自の名前空間を持つことになります。 (組み込みの名前は実際にはモジュール内に存在します。そのモジュールは builtins と呼ばれています。)

関数のローカルな名前空間は、関数が呼び出されたときに作成され、関数から戻ったときや、関数内で例外が送出され、かつ関数内で処理されなかった場合に削除されます。 (実際には、忘れられる、と言ったほうが起きていることをよく表しています。) もちろん、再帰呼出しのときには、各々の呼び出しで各自のローカルな名前空間があります。

スコープ (scope) とは、ある名前空間が直接アクセスできるような、 Python プログラムのテキスト上の領域です。 "直接アクセス可能" とは、修飾なしに (訳注: spam.egg ではなく単に egg のように) 名前を参照した際に、その名前空間から名前を見つけようと試みることを意味します。

スコープは静的に決定されますが、動的に使用されます。実行中はいつでも、直接名前空間にアクセス可能な、3つまたは4つの入れ子になったスコープがあります:

最初に探される、最も内側のスコープは、ローカルな名前を持っています。

外側の(enclosing)関数のスコープは、近いほうから順に探され、ローカルでもグローバルでもない名前を持っています。

次のスコープは、現在のモジュールのグローバルな名前を持っています。

一番外側の(最後に検索される)スコープはビルトイン名を持っています。

名前が global と宣言されている場合、その名前に対する参照や代入は全て、モジュールのグローバルな名前の入った中間のスコープに対して直接行われます。最内スコープの外側にある変数に再束縛するには、 nonlocal 文が使えます。nonlocal と宣言されなかった変数は、全て読み出し専用となります (そのような変数に対する書き込みは、単に 新しい ローカル変数をもっとも内側のスコープで作成し、外部のスコープの値は変化しません)。

通常、ローカルスコープは (プログラムテキスト上の) 現在の関数のローカルな名前を参照します。関数の外側では、ローカルスコープはグローバルな名前空間と同じ名前空間、モジュールの名前空間を参照します。クラス定義では、ローカルスコープの中にもう一つ名前空間が置かれます。

スコープはテキスト上で決定されていると理解することが重要です。モジュール内で定義される関数のグローバルなスコープは、関数がどこから呼び出されても、どんな別名をつけて呼び出されても、そのモジュールの名前空間になります。反対に、実際の名前の検索は実行時に動的に行われます --- とはいえ、言語の定義は、"コンパイル" 時の静的な名前解決の方向に進化しているので、動的な名前解決に頼ってはいけません！ (事実、ローカルな変数は既に静的に決定されています。)

Python の特徴として、global や nonlocal 文が有効でない場合は、名前に対する参照は常に最も内側のスコープに対して有効になります。 代入はデータをコピーしません。オブジェクトを名前に束縛するだけです。削除も同様で、del x は、ローカルスコープの名前空間から x に対する拘束を取り除きます。 つまるところ、新しい名前を与えるようなすべての操作は、ローカルスコープを使って行われます。 import 文、関数の定義は、モジュールや関数名をローカルスコープの名前に拘束します。

global 文を使うと、特定の変数がグローバルスコープに存在し、そこで再束縛されることを指示できます。 nonlocal 文は、特定の変数が外側のスコープに存在し、そこで再束縛されることを指示します。

9.2.1. スコープと名前空間の例
異なるスコープと名前空間がどのように参照されるか、また global および nonlocal が変数の束縛にどう影響するか、この例で実演します:

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
このコード例の出力は:

After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
このとおり、(デフォルトの) ローカルな 代入は scope_test 上の spam への束縛を変更しませんでした。 nonlocal 代入は scope_test 上の spam への束縛を変更し、 global 代入はモジュールレベルの束縛を変更しました。

またここから、 global 代入の前には spam に何も束縛されていなかったことも分かります。

9.3. クラス初見
クラスでは、新しい構文を少しと、三つの新たなオブジェクト型、そして新たな意味付けをいくつか取り入れています。

9.3.1. クラス定義の構文
クラス定義の最も単純な形式は、次のようになります:

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
関数定義 (def 文) と同様、クラス定義が効果をもつにはまず実行しなければなりません。 (クラス定義を if 文の分岐先や関数内部に置くことも、考え方としてはありえます。)

実際には、クラス定義の内側にある文は、通常は関数定義になりますが、他の文を書くこともでき、それが役に立つこともあります --- これについては後で述べます。クラス内の関数定義は通常、メソッドの呼び出し規約で決められた独特の形式の引数リストを持ちます --- これについても後で述べます。

クラス定義に入ると、新たな名前空間が作成され、ローカルな名前空間として使われます --- 従って、ローカルな変数に対する全ての代入はこの新たな名前空間に入ります。特に、関数定義を行うと、新たな関数の名前はこの名前空間に結び付けられます。

クラス定義から普通に (定義の終端に到達して) 抜けると、 クラスオブジェクト (class object) が生成されます。クラスオブジェクトは、基本的にはクラス定義で作成された名前空間の内容をくるむラッパ (wrapper) です。

クラスオブジェクトについては次の節で詳しく学ぶことにします。 (クラス定義に入る前に有効だった) 元のローカルスコープが復帰し、生成されたクラスオブジェクトは復帰したローカルスコープにクラス定義のヘッダで指定した名前 (上の例では ClassName) で結び付けられます。

9.3.2. クラスオブジェクト
クラスオブジェクトでは２種類の演算、属性参照とインスタンス生成をサポートしています。

属性参照 (attribute reference) は、Python におけるすべての属性参照で使われている標準的な構文、 obj.name を使います。クラスオブジェクトが生成された際にクラスの名前空間にあった名前すべてが有効な属性名です。従って、以下のようなクラス定義では:

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
MyClass.i と MyClass.f は妥当な属性参照であり、それぞれ整数と関数オブジェクトを返します。クラス属性に代入を行うこともできます。従って、 MyClass.i の値を代入して変更できます。 __doc__ も有効な属性で、そのクラスに属している docstring、この場合は "A simple example class" を返します。

クラスの インスタンス化 (instantiation) には関数のような表記法を使います。クラスオブジェクトのことを、単にクラスの新しいインスタンスを返す引数がない関数のように振る舞います。例えば (上記のクラスでいえば):

x = MyClass()
は、クラスの新しい インスタンス (instance) を生成し、そのオブジェクトをローカル変数 x へ代入します。

このクラスのインスタンス生成操作 (クラスオブジェクトの "呼出し") を行うと、空のオブジェクトを生成します。多くのクラスは、オブジェクトを作成する際に、カスタマイズされた特定の初期状態になってほしいと望んでいます。そのために、クラスには __init__() という名前の特別なメソッド定義することができます。例えば次のようにします:

def __init__(self):
    self.data = []
クラスが __init__() メソッドを定義している場合、クラスのインスタンスを生成すると、新しく生成されたクラスインスタンスに対して自動的に __init__() を呼び出します。従って、この例では、新たな初期済みのインスタンスを次のようにして得ることができます:

x = MyClass()
もちろん、より大きな柔軟性を持たせるために、 __init__() メソッドに複数の引数をもたせることができます。その場合、次の例のように、クラスのインスタンス生成操作に渡された引数は __init__() に渡されます。例えば、

>>>
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)


9.3.3. インスタンスオブジェクト
ところで、インスタンスオブジェクトを使うと何ができるのでしょうか？インスタンスオブジェクトが理解できる唯一の操作は、属性の参照です。有効な属性名には (データ属性およびメソッドの) 二種類あります。

データ属性 (data attribute) は、これは Smalltalk の "インスタンス変数" や C++の "データメンバ" に相当します。データ属性を宣言する必要はありません。ローカルな変数と同様に、これらの属性は最初に代入された時点で湧き出てきます。例えば、上で生成した MyClass のインスタンス x に対して、次のコードを実行すると、値 16 を印字し、 x の痕跡は残りません:

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
もうひとつのインスタンス属性は メソッド (method) です。メソッドとは、オブジェクトに "属している" 関数のことです。(Python では、メソッドという用語はクラスインスタンスだけのものではありません。オブジェクト型にもメソッドを持つことができます。例えば、リストオブジェクトには、 append, insert, remove, sort などといったメソッドがあります。とはいえ、以下では特に明記しない限り、クラスのインスタンスオブジェクトのメソッドだけを意味するものとして使うことにします。)

インスタンスオブジェクトで有効なメソッド名は、そのクラスによります。定義により、クラスの全ての関数オブジェクトである属性がインスタンスオブジェクトの妥当なメソッド名に決まります。従って、例では、MyClass.f は関数なので、x.f はメソッドの参照として有効です。しかし、MyClass.i は関数ではないので、x.i はメソッドの参照として有効ではありません。x.f は MyClass.f と同じものではありません --- 関数オブジェクトではなく、メソッドオブジェクト (method object) です。

9.3.4. メソッドオブジェクト
普通、メソッドはバインドされた直後に呼び出されます:

x.f()
MyClass の例では、上のコードは文字列 'hello world' を返すでしょう。しかしながら、必ずしもメソッドをその場で呼び出さなければならないわけではありません。 x.f はメソッドオブジェクトであり、どこかに記憶しておいて後で呼び出すことができます。例えば次のコードは:

xf = x.f
while True:
    print(xf())
hello world を時が終わるまで印字し続けるでしょう。

メソッドが呼び出されるときには実際には何が起きているのでしょうか？ f() の関数定義では引数を一つ指定していたにもかかわらず、上の例では x.f() が引数なしで呼び出されています。引数はどうなったのでしょうか？たしか、引数が必要な関数を引数無しで呼び出すと、 Python が例外を送出するはずです --- たとえその引数が実際には使われなくても…。

もう答は想像できているかもしれませんね: メソッドについて特別なこととして、インスタンスオブジェクトが関数の第1引数として渡されます。 例では、 x.f() という呼び出しは、 MyClass.f(x) と厳密に等価なものです。 一般に、 n 個の引数リストもったメソッドの呼出しは、そのメソッドのインスタンスオブジェクトを最初の引数の前に挿入した引数リストで、メソッドに対応する関数を呼び出すことと等価です。

もしまだメソッドの動作を理解できなければ、一度実装を見てみると事情がよく分かるかもしれません。インスタンスの非データ属性が参照されたときは、そのインスタンスのクラスが検索されます。その名前が有効なクラス属性を表している関数オブジェクトなら、インスタンスオブジェクトと見つかった関数オブジェクト (へのポインタ) を抽象オブジェクト、すなわちメソッドオブジェクトにパックして作成します。メソッドオブジェクトが引数リストと共に呼び出されるとき、インスタンスオブジェクトと渡された引数リストから新しい引数リストを作成して、元の関数オブジェクトを新しい引数リストで呼び出します。

9.3.5. クラスとインスタンス変数
一般的に、インスタンス変数はそれぞれのインスタンスについて固有のデータのためのもので、クラス変数はそのクラスのすべてのインスタンスによって共有される属性やメソッドのためのものです:

















9.8. イテレータ (iterator)
すでに気づいているでしょうが、 for 文を使うとほとんどのコンテナオブジェクトにわたってループを行うことができます:

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
こういう要素へのアクセス方法は明確で簡潔で使い易いものです。イテレータの活用は Python へ広く行き渡り、統一感を持たせています。裏では for 文はコンテナオブジェクトに対して iter() 関数を呼んでいます。関数は、コンテナの中の要素に1つずつアクセスする __next__() メソッドが定義されているイテレータオブジェクトを返します。これ以上要素が無い場合は、 __next__() メソッドは StopIteration 例外を送出し、その通知を受け for ループは終了します。組み込みの next() 関数を使って __next__() メソッドを直接呼ぶこともできます; この例は関数がどう働くのかを示しています:

>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x00A1DB50>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration

イテレータプロトコルの裏にある仕組みを観察していれば、自作のクラスにイテレータとしての振舞いを追加するのは簡単です。 '''__next__() メソッドを持つオブジェクトを返す __iter__() メソッドを定義する'''のです。クラスが __next__() メソッドを定義している場合、 __iter__() メソッドは単に self を返すことも可能です:

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
    # iter(rev)
    # <__main__.Reverse object at 0x00A1DB50>

for char in rev:
    print(char)
m
a
p
s


9.9. ジェネレータ (generator)
ジェネレータ は、イテレータを作成するための簡潔で強力なツールです。ジェネレータは通常の関数のように書かれますが、何らかのデータを返すときには yield 文を使います。そのジェネレータに対して next() が呼び出されるたびに、ジェネレータは以前に中断した処理を再開します (ジェネレータは、全てのデータ値と最後にどの文が実行されたかを記憶しています)。以下の例を見れば、ジェネレータがとても簡単に作成できることがわかります:

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
>>>
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g

ジェネレータでできることは、前の節で解説したクラスを使ったイテレータでも実現できます。ジェネレータの定義がコンパクトになるのは __iter__() メソッドと __next__() メソッドが自動で作成されるからです。

ジェネレータのもう一つの重要な機能は、呼び出しごとにローカル変数と実行状態が自動的に保存されるということです。これにより、 self.index や self.data といったインスタンス変数を使ったアプローチよりも簡単に関数を書くことができるようになります。

メソッドを自動生成したりプログラムの実行状態を自動保存するほかに、ジェネレータは終了時に自動的に StopIteration を送出します。これらの機能を組み合わせると、通常の関数を書くのと同じ労力で、簡単にイテレータを生成できます。


9.10. ジェネレータ式
単純なジェネレータなら式として簡潔にコーディングできます。 その式はリスト内包表記に似た構文を使いますが、角括弧ではなく丸括弧で囲います。 ジェネレータ式は、関数の中でジェネレータをすぐに使いたいような状況のために用意されています。 ジェネレータ式は完全なジェネレータの定義よりコンパクトですが、ちょっと融通の効かないところがあります。 同じ内容を返すリスト内包表記よりはメモリに優しいことが多いという利点があります。

>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
