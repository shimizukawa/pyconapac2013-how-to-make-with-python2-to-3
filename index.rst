===========================================================
Python **2.5** からPython **3.3** で 動作するツールの作り方
===========================================================

.. ================================================================
.. Introduction
.. ================================================================
.. 5分


About Me
=========
.. figure:: images/face.png

http://about.me/shimizukawa

Activity

* Sphinx co-committer
* Sphinx-users.jp chairman
* PyCon JP 2011,2012 vice-chairman

.. s6:: effect slide

.. s6:: styles

    'div[0]': {width:'15%', position:'absolute', top:'0', right:'1em'},


Books
======

* エキスパートPythonプログラミング (和訳)

  .. figure:: images/book-epp.jpg

* Pythonプロフェッショナルプログラミング (2章分)

  .. figure:: images/book-pypro.png

.. s6:: styles

   'ul/li[0]/p': {width: '50%', marginBottom:'0.5em'},
   'ul/li[0]/div': {width:'30%', position:'absolute', left:'55%', top:'1em'},
   'ul/li[1]': {marginLeft: '2em'},
   'ul/li[1]/p': {width: '50%'},
   'ul/li[1]/div': {width:'30%', position:'absolute', right:'0', top:'4em'},
   'ul/li[1]/ul/li[0]': {display:'none'},
   'ul': {fontSize:'70%'},

.. s6:: actions

   ['ul/li[1]/ul/li', 'fade in', '0.3'],

   * The books mention to Sphinx and Documentations.

   * "Python Professional Programming" was already translated into
     'simple chineese charactors' and will publish in June. (This is chneese

中国語版
================

.. figure:: images/book-pypro-china.png
   :width: 50%
   :align: center

   10月に発売予定らしい

Sphinxをはじめよう
==================

.. figure:: images/book-learn-sphinx.jpg

   Sphinxをはじめよう

* 謎の動物
* 世界初のSphinx本（多分）
* オライリー・ジャパンさん
* 電子書籍
* 100P弱相当
* 1,680円
* **Now ON SALE !!**

.. s6:: styles

   'p': {width: '50%', marginBottom:'0.5em'},
   'div': {width:'40%', position:'absolute', left:'58%', top:'1em'},
   'ul': {marginLeft: '2em'},
   'ul': {width: '50%'},
   'ul': {width:'30%', position:'absolute', right:'0', top:'4em'},
   'ul': {fontSize:'70%'},

Abstract
=========

.. s6:: styles

   'h2': {textAlign:'center', margin:'30% auto', lineHeight:'1.5em'}

Abstract
=========

目的
  多数のPythonバージョンで動作するようにコードを書く

対象環境:
  Python2.5 - Python3.3 (3.0を除く)

題材:
  sphinx-intl

.. s6:: effect slide

.. s6:: styles

   'dl': {fontSize:'90%'},

.. ================================================================
.. What is sphinx-intl
.. ================================================================
.. 5分

What is sphinx-intl
====================

* Sphinxの国際化機能サポートツール

  * potから言語別poの生成、更新、ビルド
  * transifexサポート: potからtransifex設定ファイルの生成

.. todo:: sphinxとpotの絵

.. sphinx-intlがなんのためのツールかということを端的に説明したいが、この文面だと長い：「sphinx-users.jpで使用している手法について紹介します。この方法は、ドキュメントの更新があれば自動的にpoファイルを更新してくれるし、翻訳文を更新すれば自動的にサイトを更新してくれる全自動の手法です。この手法の中核にあるのがsphinx-intlです。」

.. s6:: effect slide

Motivation
===========

* SphinxがPython2.5から3.3まで対応(3.0除く)
* sphinx-intlも同じバージョン対応が必要


.. s6:: effect slide

Detail of sphinx-intl
======================

* sphinx-intlの行数:

  * 本体: 577行 （docstring含む）
  * ドキュメント: 229行 （README等）
  * テスト: 500行 （ユーティリティ含む）

* sphinx-intlの構成:

  * TODO: 簡単なツリー構造を書く

.. s6:: effect slide



.. ================================================================
.. Difference from Python2.5 to Python 3.3
.. ================================================================
.. 15分

Difference from Python2.5 to Python 3.3
=======================================

.. s6:: styles

   'h2': {textAlign:'center', margin:'30% auto', lineHeight:'1.5em'}

Difference from Python2.5 to Python 3.3
=======================================

* ライブラリの違い
* 関数の違い
* 文法の違い

sphinx-intlが使っている範囲で紹介

.. speech:: ライブラリや関数の違いを吸収するのは簡単ですが、文法の違いを吸収するのは手間がかかります。どこが違って、どうやって吸収するのかについて、sphinx-intlが使用している範囲で紹介します。

.. s6:: effect slide

Python2か3かを見分ける
======================

バージョン番号判別

.. code-block:: pycon

   >>> PY2 = sys.version_info < (3, 0)
   >>> PY3 = not PY2
   >>> PY2
   True
   >>> PY3
   False

.. s6:: effect slide

ライブラリの違い
================

* optparse(まだある)とargparse(2.7以降, 3.2以降)
* OrderedDict(2.7から)

.. s6:: effect slide

関数や属性の変更
=================

* unicodeとstrとbytes (2と3で異なる)
* func_code (2のみ)と__code__ (2.6以降)
* callable消滅 (3.0, 3.1のみ、3.2で復活)
* execfile消滅 (3.0以降)

.. s6:: effect slide

関数: unicodeとstrとbytes
==========================

* Python2の str() は Python3の bytes()
* Python2の unicode() は Python3の str()

.. code-block:: python

   if PY3:
       def b(s):
           return s.encode("latin-1")
       def u(s):
           return s
   else:
       def b(s):
           return s
       def u(s):
           return unicode(s, "unicode_escape")

.. s6:: effect slide

属性: func_codeと__code__
==========================

関数オブジェクトの属性。

.. code-block:: python

   def spam(name, age, kind=None):
       pass

関数の引数の数や変数前とか色々取れる。

.. code-block:: python

   if PY3:
       argcount = spam.__code__.co_argcount
       varnames = spam.__code__.co_varnames[:argcount]
   else:
       argcount = spam.func_code.co_argcount
       varnames = spam.func_code.co_varnames[:argcount]

.. s6:: effect slide

.. s6:: styles

   'div': {fontSize:'75%'}


関数: callable消滅
===================

* 3.0で組み込み関数から消えた
* 3.2で復活した

.. code-block:: python

   try:
       callable = callable

   except NameError:
       def callable(obj):
           return any(
               "__call__" in klass.__dict__
               for klass in type(obj).__mro__
           )

.. s6:: styles

   'div': {fontSize:'85%'}

.. s6:: effect slide

関数: execfile消滅
==================

* 3.0で組み込み関数から消えた

.. code-block:: python

   try:
       execfile = execfile

   except NameError:
       def execfile(filepath, _globals):
           f = open(filepath, 'rt')
           source = f.read()
           code = compile(source, filepath, 'exec')
           exec(code, _globals)

execもPy3で文から式に変わりました。

.. s6:: styles

   'div': {fontSize:'80%'}

.. s6:: effect slide

文法の違い
==========

* with文
* print文とprint関数

.. s6:: effect slide


文法: with文
=============

* 2.5から__future__で提供、2.6から標準

.. code-block:: python

   from __future__ import with_statement

   with open('file.txt', 'r') as f:
      print f.read()


.. s6:: effect slide

文法: print文とprint関数
========================

* 2.6から__future__でprint関数提供、3.0から標準

.. code-block:: pycon

   >>> print('spam', 'egg', 'ham')
   ('spam', 'egg', 'ham')

Python2ではタプルをprintしてしまう

.. code-block:: python

   from __future__ import print_function

2.5では使えない。print関数は仕様が多いので、互換機能実装はとても面倒。

.. s6:: effect slide


.. ================================================================
.. How to compatible with both python2 and 3
.. ================================================================
.. 20分

How to compatible with both python2 and 3
=========================================

.. speech:: 2to3を使ってコード変換する方法と、sixを使って共通コードで動作させる方法があります。一長一短ありますが、どのようなときにどちらを使うべきかなど紹介します。

.. s6:: styles

   'h2': {textAlign:'center', margin:'30% auto', lineHeight:'1.5em'}

.. s6:: effect slide

How to compatible with both python2 and 3
=========================================

* 2to3を使う
* 自力で両対応のコードを書く
* sixを使う

2to3を使う
===========

Python3にはlib2to3がある

良いこと

* Python2のコードを自動的にPython3コードに変換してくれる
* 最新のsetuptoolsはsetup(2to3=True)でインストール時変換できる

悪いこと

* 2to3は遅い
* テスト実行のために毎回2to3が必要
* Python3でだけエラーがある場合、変換後のコードで問題があると面倒
  (どう変換されるか予測してPython2のコードを書く必要があったり)

.. s6:: effect slide

両方で解釈できる方法で書く
==========================

2to3を使わず、両方で解釈できる方法で書く。

良いこと

* 2to3の問題点が発生しない！（変換無い、デバッグしやすい）
* Python2.6以降なら大体Python3互換の書き方ができる

悪いこと

* Python2.4対応は絶望的（可能だけど）
* Python2.5を投げ捨てたくなる
* 差異の吸収を自分でやる手間がかかる

.. s6:: effect slide

sphinx-intlはどうしたか？
==========================

* 最初は自力で両対応コードを書いていた
* printとexecの互換実装が面倒
* エクササイズのつもりだったけど面倒になった
* 諦めてsixを導入

.. s6:: effect slide

six
=====

* 2013/9/1: 1.4 released
* Python2.4から3.3まで対応
* 移動したり名前が変わったり消えたり増えたりしたパッケージ、モジュールの互換レイヤ
* 移動や名前変更は内部でバージョン判別して呼び直している（要コードサンプル）
* 消えたり増えたりは、同一機能を提供（要コードサンプル）

.. s6:: effect slide

避けられない自力対応
====================

* sixでも提供されていないexecfileは自力で対応

.. s6:: effect slide


避けられない2to3 (conf.py)
===========================

* sphinx-intlはSphinxのconf.pyを読んでいる(locale等の設定を見るため)
* conf.pyはユーザーが書くので、Python2か3か分からない
* 読み込めたらそのまま使う、だめなら2to3で変換してもう一度読み込む

こういうこともあるんだね

.. s6:: effect slide

.. ================================================================
.. パッケージングにおける課題
.. ================================================================
.. 10分

パッケージングにおける課題
==========================

.. speech:: 2013/7/1現在、Pythonのパッケージングは混乱しています。とりあえず今どうすると安定したパッケージ供給が出来るのか紹介します。

.. s6:: styles

   'h2': {textAlign:'center', margin:'30% auto', lineHeight:'1.5em'}

.. s6:: effect slide

パッケージングにおける課題
==========================

* パッケージングツールの変遷
* setuptoolsを使うか、使わないか
* Python2と3で動作するsetup.pyを作る


.. s6:: effect slide

パッケージングツールの変遷
===================================

1. Python標準はdistutils、色々足りないしeasy_install的なのが無い
2. setuptoolsがeasy_installを提供
3. pipはeasy_installより便利なコマンドを提供
4. setuptoolsをPython3対応させたdistributeがデファクトに

ここまでがPyCon JP 2011の頃。

.. s6:: effect slide

2012年
======

* setuptoolsはもう更新されてないから ``distribute`` 使おう！
* Python3.3で提供される ``packaging`` を使おう！
* packagingがPython3.3リリース直前に消滅

これがPyCon JP 2012の前後。

.. s6:: effect slide

2013年
======

* ``distlib`` 登場。packagingで不足していた下位レイヤ。Python3.4同梱予定。
* ``wheel`` 登場。eggに代わるPython標準のバイナリ形式。distlibと合流。
* ``distribute`` 廃止！ ``setuptools`` に統合。setuptoolsがPython3対応に！

**setuptoolsを使おう！** （distlibの世界になるまでは）

詳しくは `PyCon APAC 2013 DAY1, パッケージングの今と未来`_ の発表を参照

.. _PyCon APAC 2013 DAY1, パッケージングの今と未来: session-14-1110-rooma0715-ja1-ja

.. s6:: effect slide

Python2と3で動作するsetup.pyを作る
===================================

* setup.pyはPython2,3互換コードで書く
* 特定バージョンの場合だけ依存パッケージをインストールする
* 特定バージョンの場合、依存パッケージのバージョンを指定する

.. s6:: effect slide

まとめ
=======

.. s6:: styles

   'h2': {textAlign:'center', margin:'30% auto', lineHeight:'1.5em'}

.. s6:: effect slide

まとめ
=======

* 

