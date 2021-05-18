デバッグ、アルゴリズムが持つインスタンス情報を知りたいときのシート

予約語を調べる時
import keyword

予約語であるかどうか一覧で確認
keyword.kwlist

'etc'という単語が予約語かどうか確認したい時
keyword.iskeyword('etc')

インスタンス情報を取得したい時

機械学習でクラスを調べるときに頻繁に使いそうだったのでメモ。

### インスタンスが持つインスタンス変数の一覧を取得する

```
# .__dict__属性を取得
class hoge:
    def __init__(self,x,y):
        self.x = x
        self.y = y

ins_sample = hoge(30,20)


from pprint import pprint
# モジュール、クラス、インスタンス、あるいはそれ以外の dict 属性を持つオブジェクトの、 dict 属性を返す
pprint(vars(ins_sample),width=100)
# {'x': 30, 'y': 20}
# そのオブジェクトの有効な属性のリストを返そうと試みる
pprint(ins_sample.__dict__)
# {'x': 30, 'y': 20}

### ex.PCA(主成分分析)においてインスタンスが持つインスタンス変数を調べる

from sklearn.decomposition import PCA

PCA = PCA()

X_demo = np.append(X0,X1, axis =1) + np.random.normal(loc = 0, scale=15, size=200).reshape(100,2)

PCA.fit(X_demo) 
pc = PCA.transform(X_demo)

# モジュール、クラス、インスタンス、あるいはそれ以外の dict 属性を持つオブジェクトの、 dict 属性を返します
pprint(vars(PCA),width=100)

{'_fit_svd_solver': 'full',
 'components_': array([[ 0.31587351,  0.94880131],
       [-0.94880131,  0.31587351]]),
 'copy': True,
 'explained_variance_': array([9245.73144191,  190.24761265]),
 'explained_variance_ratio_': array([0.97983806, 0.02016194]),
 'iterated_power': 'auto',
 'mean_': array([ 47.17932959, 147.75046498]),
#  X_demo.mean(axis=0) --> array([ 47.17932959, 147.75046498])

 'n_components': None,
 'n_components_': 2, # 主成分の数
 'n_features_': 2,
 'n_features_in_': 2,
 'n_samples_': 100,
 'noise_variance_': 0.0,
 'random_state': None,
 'singular_values_': array([956.72744956, 137.23889264]),
 'svd_solver': 'auto',
 'tol': 0.0,
 'whiten': False}
# そのオブジェクトの有効な属性のリストを返そうと試みます
pprint(PCA.__dict__)


# オブジェクトが持つ属性のリストを取得したい
dir([object])
引数がない場合、現在のローカルスコープにある名前のリストを返します。引数がある場合、そのオブジェクトの有効な属性のリストを返そうと試みます。

pprint(dir(X_demo)) # shape属性？メソッドやmean属性？メソッドを持っていることが分かる
['T',
 '__abs__',
 '__add__',
 '__and__',
 '__array__',
 '__array_finalize__',
 '__array_function__',
 '__array_interface__',
 '__array_prepare__',
 '__array_priority__',
 '__array_struct__',
 '__array_ufunc__',
 '__array_wrap__',
 '__bool__',
 '__class__',
 '__complex__',
 '__contains__',
 '__copy__',
 '__deepcopy__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__divmod__',
 '__doc__',
 '__eq__',
 '__float__',
 '__floordiv__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__iand__',
 '__ifloordiv__',
 '__ilshift__',
 '__imatmul__',
 '__imod__',
 '__imul__',
 '__index__',
 '__init__',
 '__init_subclass__',
 '__int__',
 '__invert__',
 '__ior__',
 '__ipow__',
 '__irshift__',
 '__isub__',
 '__iter__',
 '__itruediv__',
 '__ixor__',
 '__le__',
 '__len__',
 '__lshift__',
 '__lt__',
 '__matmul__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__new__',
 '__or__',
 '__pos__',
 '__pow__',
 '__radd__',
 '__rand__',
 '__rdivmod__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rfloordiv__',
 '__rlshift__',
 '__rmatmul__',
 '__rmod__',
 '__rmul__',
 '__ror__',
 '__rpow__',
 '__rrshift__',
 '__rshift__',
 '__rsub__',
 '__rtruediv__',
 '__rxor__',
 '__setattr__',
 '__setitem__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__truediv__',
 '__xor__',
 'all',
 'any',
 'argmax',
 'argmin',
 'argpartition',
 'argsort',
 'astype',
 'base',
 'byteswap',
 'choose',
 'clip',
 'compress',
 'conj',
 'conjugate',
 'copy',
 'ctypes',
 'cumprod',
 'cumsum',
 'data',
 'diagonal',
 'dot',
 'dtype',
 'dump',
 'dumps',
 'fill',
 'flags',
 'flat',
 'flatten',
 'getfield',
 'imag',
 'item',
 'itemset',
 'itemsize',
 'max',
 'mean',
 'min',
 'nbytes',
 'ndim',
 'newbyteorder',
 'nonzero',
 'partition',
 'prod',
 'ptp',
 'put',
 'ravel',
 'real',
 'repeat',
 'reshape',
 'resize',
 'round',
 'searchsorted',
 'setfield',
 'setflags',
 'shape',
 'size',
 'sort',
 'squeeze',
 'std',
 'strides',
 'sum',
 'swapaxes',
 'take',
 'tobytes',
 'tofile',
 'tolist',
 'tostring',
 'trace',
 'transpose',
 'var',
 'view']
```

おまけ
予約語を調べる時

```
import keyword

予約語であるかどうか一覧で確認
keyword.kwlist

'etc'という単語が予約語かどうか確認したい時
keyword.iskeyword('etc')
```

インスタンス情報を取得したい時
