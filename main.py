from deck import stock
from poker import Poker


class Player:
    """
    メインゲーム（インスタンス作成時にplayerとdealerインスタンス作成）
    """

    def __init__(self):
        self.money = 100
        self.hands = []

    def draw_card(self, deck, num=1):
        """
        カードをデッキからドローし手札に加える
        ※異なる枚数がドローされてもok

        Parameters
        ----------
        num : int, default 1
            カードをドローする回数

        Examples
        --------
        >>> player.draw_card(2) # 2枚ドロー [♠︎-J, ♠︎-10]
        >>> player.draw_card(3) # [♦︎-9, ♣️-10, ♠︎-2]
        >>> print(player.hands)
        [♠︎-J, ♠︎-10, ♦︎-9, ♣️-10, ♠︎-2]
        """
        self.hands_store = deck.pick_card(num)
        self.hands.extend(self.hands_store)


class Game:
    """
    メインゲーム（インスタンス作成時にplayerとdealerインスタンス作成）

    Examples
    --------
    >>> game = Game()
    >>> game.main() # ゲームスタート（下記の初期フェーズが表示）

    """

    RANKS = (*"23456789", "10", *"JQKA")
    VALUES = (range(2, 14 + 1))
    # 表示マークとスコアを紐づける
    RANK_TO_VALUES = dict(zip(RANKS, VALUES))

    def __init__(self):
        # player作成
        self.player = Player()
        self.is_poker_win = False

    def doubleUp_game(self):
        """
        ダブルアップチャンス
        """
        print("double-Up Chance Game start")

    def main(self):
        """
        ゲーム全体（ポーカー + ダブルアップチャンス）
        """

        # 山札セット（セット数を決める）
        deck = stock.Deck()
        poker = Poker(deck, self.player)
        poker.main_game()
        # self.poker_game(deck)

        # 役ありはダブルアップチャンス
        if self.is_poker_win:
            self.doubleUp_game()


if __name__ == '__main__':
    game = Game()
    game.main()
