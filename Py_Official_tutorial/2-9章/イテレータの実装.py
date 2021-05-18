class Container:
     pass
for 文の in に使えるようにします（  iterable  にします）。 最も小さい iterable を実装していきます。

>>> # 何も起こらない。とにかくエラーが発生しないことを目標に。
>>> for element in Container():
...     print(element)
>>> 