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


.. s6:: effect slide

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
     version book name).


.. Learning Sphinx
.. ================
.. 
.. * Sphinxをはじめよう (1.5章分)
.. 
..   .. figure:: images/book-sphinx.jpg
.. 
.. * 販売開始は **本日** から！！
.. 
..   * オライリー・ジャパンさんより
..   * 電子書籍のみ
..   * 金額？


Abstract
=========

趣旨:
  多数のPythonバージョンで動作するコードの書き方

対象環境:
  Python2.5 - Python3.3 (3.0を除く)

題材:
  sphinx-intl


.. s6:: effect slide

.. s6:: styles

   'dl': {fontSize:'90%'},

.. speech::

   sphinx-intlを題材に、Python2.5からPython3.3までの環境で動作するプログラムの書き方について紹介します。


Motivation
===========

* sphinx-intlはSphinxの国際化機能サポートツール
* SphinxがPython2.5から3.3まで対応している(3.0除く)
* 同じバージョン対応が必要
* 2to3でコード変換する方法はテストなど面倒
* sixを使って2to3変換無しで動作させよう
* sixでサポートしていない一部の非互換コードは自作


.. ================================================================
.. What is sphinx-intl
.. ================================================================
.. 5分

What is sphinx-intl
===================

* sphinx-intlはどんなツール？
* 機能:

  * potから言語別poの生成、更新、ビルド
  * transifexサポート: potからtransifex設定ファイルの生成

* 行数:

  * 本体: 577行 （docstring含む）
  * ドキュメント: 229行 （README等）
  * テスト: 500行 （ユーティリティ含む）

.. todo:: 全体把握のため、簡単なツリー構造あったほうがいいかな


.. sphinx-intlがなんのためのツールかということを端的に説明したいが、この文面だと長い：「sphinx-users.jpで使用している手法について紹介します。この方法は、ドキュメントの更新があれば自動的にpoファイルを更新してくれるし、翻訳文を更新すれば自動的にサイトを更新してくれる全自動の手法です。この手法の中核にあるのがsphinx-intlです。」


.. ================================================================
.. Difference from Python2.5 to Python 3.3
.. ================================================================
.. 15分

Difference from Python2.5 to Python 3.3
=======================================

ライブラリや関数の違いを吸収するのは簡単ですが、文法の違いを吸収するのは手間がかかります。どこが違って、どうやって吸収するのかについて紹介します。

* Python2か3かを見分ける

  * ``sys.version_info < (3, 0)``
  * Python2ならTrue

* ライブラリの違い

  * optparse(まだある)とargparse(2.7以降, 3.2以降)
  * OrderedDict(2.7から)

* 関数や属性の違い

  * unicodeとstrとbytes (2と3で異なる)
  * func_code (2のみ)と__code__ (2.6以降)
  * execfile消滅 (3.0以降)
  * callable消滅 (3.0, 3.1のみ)

* 文法の違い

  * with文 (2.5で__future__で提供、2.6以降標準)
  * print文とprint関数 (3.0/2.6)
  * u'' と b'' (3.3/3.0/2.6)


.. todo:: 文法の違いとしてsphinx-intlで扱っているものだけでよいか？もっと一般的な何かを紹介したほうがよいか？割り算の整数？next()


.. ================================================================
.. How to compatible with both python2 and 3
.. ================================================================
.. 20分

How to compatible with both python2 and 3
=========================================

2to3を使ってコード変換する方法と、sixを使って共通コードで動作させる方法があります。一長一短ありますが、どのようなときにどちらを使うべきかなど紹介します。

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

2to3を使わない
===============

両方で解釈できる方法で書く

良いこと

* 2to3の問題点が発生しない！（変換無い、デバッグしやすい）
* Python2.6以降なら大体Python3互換の書き方ができる

悪いこと

* Python2.4対応は絶望的（可能だけど）
* Python2.5を投げ捨てたくなる
* 差異の吸収を自分でやる手間がかかる


sphinx-intlはどうしたか？
==========================

* 最初はsix無しで書いていた
* printとexecの互換実装が面倒
* six万歳
* sixでも提供されていないexecfileは自力で対応

six
=====

* 2013/9/1: 1.4 released
* Python2.4から3.3まで対応
* 移動したり名前が変わったり消えたり増えたりしたパッケージ、モジュールの互換レイヤ
* 移動や名前変更は内部でバージョン判別して呼び直している（要コードサンプル）
* 消えたり増えたりは、同一機能を提供（要コードサンプル）


避けられない2to3 (conf.py)
===========================

* sphinx-intlはSphinxのconf.pyを読んでいる(locale等の設定を見るため)
* conf.pyはユーザーが書くので、Python2か3か分からない
* 読み込めたらそのまま使う、だめなら2to3で変換してもう一度読み込む

こういうこともあるんだね


.. ================================================================
.. パッケージングにおける課題
.. ================================================================
.. 10分

パッケージングにおける課題
==========================

2013/7/1現在、Pythonのパッケージングは混乱しています。とりあえず今どうすると安定したパッケージ供給が出来るのか紹介します。

パッケージングツールの変遷
===================================

* Python標準はdistutils、色々足りないしeasy_install的なのが無い
* setuptoolsがeasy_installを提供
* pipはsetuptoolsを使って便利なインストーラコマンドを提供
* setuptoolsをPython3対応させたdistributeがデファクトに

2 years ago (2011/9)
=====================

* setuptoolsはもう更新されてないから ``distribute`` 使おう！
* Python3.3で提供される ``packaging`` を使おう！


1 years ago (2012/9)
=====================

* setuptoolsはもう更新されてないから ``distribute`` 使おう！
* packagingがPython3.3リリース直前に消滅..

6 months ago (2013/3)
======================

* setuptoolsはもう更新されてないから ``distribute`` 使おう！
* ``distlib`` リリース、packagingで不足していた下位レイヤーを提供
* ``wheel`` というeggに代わるPython標準のバイナリフォーマット登場

1 month ago (2013/8)
=====================

* distributeは廃止されsetuptoolsに統合されPython3にも対応！ ``setuptools`` を使おう！
* ``distlib`` がsetuptoolsの機能をほぼ全て提供しつつある（互換性は基本的にない）
* ``distlib`` は2014年頭にリリースのPython3.4に同梱予定

Today (2013)
=============

* setuptoolsが0.7以降リリース乱発、もう1.1.4まで来た
* setuptools大丈夫か？はやくdistlib使える世界になって欲しい


setuptoolsを使うか、使わないか
===============================

* 今はまだsetuptoolsがデファクトスタンダード
* setuptools自体は既存資産を使うために今後も必要
* まだしばらくはsetuptoolsとつきあっていく必要あり

詳しくは `PyCon APAC 2013 DAY1, パッケージングの今と未来`_ の発表を参照

.. _PyCon APAC 2013 DAY1, パッケージングの今と未来: session-14-1110-rooma0715-ja1-ja

Python2と3で動作するsetup.pyを作る
===================================

* setup.pyはPython2,3互換コードで書く
* 特定バージョンの場合だけ依存パッケージをインストールする
* 特定バージョンの場合、依存パッケージのバージョンを指定する

