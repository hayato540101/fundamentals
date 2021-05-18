https://docs.python.org/ja/3/tutorial/classes.html

クラスは後でやる









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
