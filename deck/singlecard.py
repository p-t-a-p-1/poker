class Card:
    """
    カードのマークと数字を出力

    Attributes
    ----------
    card_mark : int
        カードのマーク（♠︎❤︎♦︎♣️）
    card_number : int
        カードの数字
    """

    # トランプのマーク
    MARKS = ("♠︎", "❤︎", "♦︎", "♣️")
    # カードの順位 - 表示用
    # ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    RANKS = (*"A23456789", "10", *"JQK")
    # カードの順位を数値化
    NUMBERS = (range(1, 13 + 1))
    # 数字と表示用のランクを紐づける
    NUMBER_TO_RANK = dict(zip(NUMBERS, RANKS))

    def __init__(self, card_mark, card_number):
        """
        Parameters
        ----------
        card_mark : int
            カードのマーク（♠︎❤︎♦︎♣️）
        card_number : int
            カードの数字
        """
        self.mark = card_mark
        self.number = card_number
        self.rank = self.NUMBER_TO_RANK[self.number]
        self.pair = f"{self.MARKS[self.mark]}-{self.rank}"

    def __repr__(self):
        """
        オーバーライドしてインスタンスの出力内容を変更

        Returns
        -------
        マークと数字が連結された文字列

        Examples
        --------
        >>> card = Card(2, 4)
        >>> print(card)
        ♦︎4
        """
        return self.pair


# Cardクラスからインスタンスを生成（引数にマークと数字）
# reprメソッドで出力内容を変更しているので下記のように出力される
# 通常 → <__main__.Card object at 0x10c949310>
# reprメソッド追加 → ♦︎-4

if __name__ == '__main__':
    card = Card(2, 12)
    print(card)
