# ゲームの流れ

ポーカーで役を作る → ダブルアップゲームでスコアを倍にしていく
というのが基本的な流れです。


# 機能要件

## 基本

* デッキはポーカー、ダブルアップゲーム共に毎回リセット
* プレイヤーの初期スコアは0
* ポーカー終了後、1ペア以上の役があればダブルアップゲームスタート
* ジョーカーはなし

## ポーカー

1. 5枚のカードが配られる
2. 1枚ずつ 変える or 残す を選択
3. 変える を選択したカードを交換
4. 交換後の5枚で役の計算
5. 役の判定を行い、役に応じてスコア決定

## ダブルアップゲーム

1. 5枚のカードが配られる（1枚は表向き、4枚は裏向き）
2. 4枚の裏向きのカードから表向きのカードよりも強いと思うカードを選択
    1. 強い場合はスコアが倍、再度ダブルアップゲームに挑戦できる
    2. 弱い場合はスコアが0、ポーカーから再スタート


# 役・スコアについて
| 役名 | カードの状態 | 手札の例 | スコア |
:---:|:---:| :---: |:---:
| 1ペア | 同じ数字のペアが1つ |  [♣️-4, ♠︎-4, ♦︎-Q, ♠︎-K, ❤︎-5]  | 50 |
| 2ペア | 同じ数字のペアが2つ |  [♣️-4, ♠︎-4, ♦︎-Q, ♠︎-Q, ❤︎-5]  | 100 |
| 3カード | 同じ数字3枚 |  [♣️-4, ♠︎-4, ♦︎-4, ♠︎-Q, ❤︎-5]  | 200 |
| ストレート | 数字が連続している |  [♣️-3, ♠︎-4, ♦︎-5, ♠︎-6, ❤︎-7]  | 300 |
| フラッシュ | マークが全て同じ |  [♠︎-3, ♠︎-4, ♠︎-5, ♠︎-Q, ♠︎-9]  | 400 |
| フルハウス | 同じ数字3枚 + 1ペア |  [♠︎-3, ♠︎-4, ♠︎-5, ♠︎-Q, ♠︎-9]  | 500 |
| フォーカード | 同じ数字4枚 |  [♠︎-4, ♦︎-4, ♠︎-4, ♣️-4, ❤︎-9]  | 1000 |
| ストレートフラッシュ | フラッシュ かつ ストレート |  [♠︎-4, ♠︎-5, ♠︎-6, ♠︎-7, ♠︎-8]  | 2000 |
| ロイヤルストレートフラッシュ | フラッシュ かつ ストレート |  [♠︎-10, ♠︎-J, ♠︎-Q, ♠︎-K, ♠︎-A]  | 10000 |

※ 今回はジョーカーなしで実装するのでファイブカードはなし

# 実行例
```
$ python main.py
Poker Game start

player's hands：[❤︎-4, ♠︎-9, ♣️-4, ♠︎-3, ♠︎-2]
Enter "y" to replace the card.
❤︎-4：
♠︎-9： y
♣️-4：
♠︎-3： y
♠︎-2： y
player's hands：[❤︎-4, ❤︎-K, ♣️-4, ♠︎-K, ♣️-6]
2ペア

double-Up Chance Game start
Now, your score is 100 points.
player's hands：♠︎-6, *-*, *-*, *-*, *-*
1：*-*
2：*-*
3：*-*
4：*-*
Enter a card number that is stronger than ♠︎-6： 2
Selected card is ❤︎-12
win!
200

double-Up Chance Game start
Now, your score is 200 points.
player's hands：♠︎-K, *-*, *-*, *-*, *-*
1：*-*
2：*-*
3：*-*
4：*-*
Enter a card number that is stronger than ♠︎-K： 3
Selected card is ♦︎-2
lose..
0

Qでゲーム終了、それ以外でゲームスタート：Q
```

## ローカル動作方法

pythonのバージョンは3.8以降を想定しております。

```
python main.py
```
