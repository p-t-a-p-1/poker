# Cardクラス
from deck import singlecard
# リストの要素をシャッフル
from random import shuffle


class Deck:
    """
    52枚のトランプカード（1デッキ）を作成

    Attributes
    ----------
    deck_set_no : int
        デッキの個数

    Examples
    --------
    >>> deck = Deck(2) # 2つ分のデッキ
    >>> print(deck.cards)
    [♦︎-12, ♠︎-3, ♦︎-13, ❤︎-9, ♦︎-3, ♦︎-8, ♠︎-11, ♦︎-13, ♣️-9, ♦︎-11,
     ♦︎-12, ♠︎-2, ♠︎-8, ❤︎-10, ♦︎-4, ♦︎-9, ♣️-10, ♣️-4, ♦︎-9, ♠︎-6,
     ♠︎-3, ♣️-12, ♠︎-12, ❤︎-13, ♣️-11, ♣️-8, ♦︎-10, ♦︎-5, ♦︎-7, ❤︎-12,
     ♣️-8, ♦︎-10, ♣️-10, ♦︎-6, ♠︎-9, ♦︎-5, ❤︎-12, ♠︎-12, ♠︎-10, ♣️-1,
     ♣️-3, ❤︎-1, ❤︎-9, ❤︎-3, ❤︎-6, ♠︎-8, ♦︎-1, ♠︎-13, ❤︎-3, ♦︎-2, ♣️-1,
     ♣️-12, ♠︎-7, ❤︎-8, ♣️-5, ♠︎-9, ♣️-4, ♠︎-10, ❤︎-11, ❤︎-4, ♣️-11,
     ♠︎-4, ♣️-7, ❤︎-7, ❤︎-6, ♣️-3, ♣️-9, ♦︎-2, ♦︎-11, ❤︎-5, ❤︎-4, ♠︎-13,
     ♠︎-4, ♣️-13, ♠︎-1, ♦︎-1, ♠︎-2, ♦︎-8, ❤︎-8, ♣️-5, ♣️-6, ♠︎-7, ♣️-7,
     ♠︎-11, ♠︎-6, ♠︎-5, ♦︎-6, ❤︎-5, ♣️-6, ♣️-13, ❤︎-7, ♦︎-7, ❤︎-10, ❤︎-11,
     ♠︎-5, ❤︎-2, ❤︎-13, ♦︎-3, ♠︎-1, ❤︎-1, ♦︎-4, ♣️-2, ❤︎-2, ♣️-2]
    """

    def __init__(self, deck_set_count=1):
        """
        Parameters
        ----------
        deck_set_count : int, default 1
            デッキの個数
        """

        # cardsに追加
        self.cards = [singlecard.Card(mark, value)
                      for index in range(deck_set_count)
                      for mark in range(len(singlecard.Card.MARKS))
                      for value in range(1, len(singlecard.Card.NUMBERS) + 1)]

        # デッキをシャッフル
        shuffle(self.cards)

    def pick_card(self, num=1):
        """
        要素を取得しリストから削除

        Parameters
        ----------
        num : int, default 1
            取得するカードの枚数

        Examples
        --------
        >>> print(deck.get_card(5)) # カードを5枚引く
        [♣️-2, ❤︎-2, ♣️-2, ♦︎-4, ❤︎-1]
        """
        self.card_list = []
        if len(self.cards) == 0:
            # カードが0枚の時は何もしない
            return

        # card_numの回数分カードを引く
        self.card_list = [self.cards.pop() for index in range(num)]
        return self.card_list


if __name__ == '__main__':
    deck = Deck(2)
    print(deck.cards)
    print(deck.pick_card(5))
