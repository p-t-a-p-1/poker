from deck import stock
from poker import Poker
from bonus import DoubleUp

class Player:
    """
    メインゲーム（インスタンス作成時にplayerとdealerインスタンス作成）
    """

    def __init__(self):
        self.score = 100
        self.hands = []
        self.is_poker_win = True

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

    def main(self):
        """
        ゲーム全体（ポーカー + ダブルアップチャンス）
        """
        can_play_game = True

        while can_play_game:

            # ゲームごとにplayer情報リセット
            player = Player()

            # 山札セット（セット数を決める） = ゲームごとに山札再構築
            deck = stock.Deck()
            poker = Poker(deck, player)
            poker.main_game()

            # 役ありはダブルアップチャンス
            print(player.is_poker_win)
            if player.is_poker_win:
                bonus_game = DoubleUp(player)
                bonus_game.main_game()

            # ゲームリスタート
            restart_msg = "Qでゲーム終了、それ以外でゲームスタート："
            start_res = input(restart_msg)
            if start_res == 'Q':
                can_play_game = False


if __name__ == '__main__':
    game = Game()
    game.main()
