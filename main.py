from deck import stock


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

    RANKS = (*"A23456789", "10", *"JQK")
    VALUES = (range(1, 13 + 1))
    # 表示マークとスコアを紐づける
    RANK_TO_VALUES = dict(zip(RANKS, VALUES))

    def __init__(self):
        # player作成
        self.player = Player()
        self.is_poker_win = False

    def poker_game(self):
        """
        ポーカー
        """

        print("Poker Game start")

        # 山札セット（セット数を決める）
        deck = stock.Deck()

        # 最初は5枚ドロー
        self.player.draw_card(deck, 5)

        # 初期カード表示
        print(f"player's hands：{self.player.hands}")

        # それぞれのカードを「のこす」か「かえる」のどちらかを選択
        print("Enter \"y\" to replace the card.")

        check_hands = []
        for card_idx, change_card in enumerate(self.player.hands):
            change_card_msg = f"{change_card}："
            change_card_res = input(change_card_msg)

            # 変える場合は山札からドローしてカードを交換
            if change_card_res == "y":
                change_card = deck.pick_card(1)[0]
                self.player.hands[card_idx] = change_card

            # 連想配列に追加
            check_card_set = str(change_card).split("-")
            # ❤︎
            card_mark = check_card_set[0]
            # K
            card_rank = check_card_set[1]
            # 13
            card_number = self.RANK_TO_VALUES[card_rank]
            # チェック用の辞書に追加
            check_hands.append({
                "mark": card_mark,
                "rank": card_rank,
                "number": card_number
            })

        # 交換後のカード表示
        print(f"player's hands：{self.player.hands}")

        # 昇順にソート
        check_hands_sorted = sorted(check_hands, key=lambda x: x["number"])

        # 役の確認
        for check_card in check_hands_sorted:
            print(check_card)

        self.is_poker_win = True

    def doubleUp_game(self):
        """
        ダブルアップチャンス
        """
        print("double-Up Chance Game start")

    def main(self):
        """
        ゲーム全体（ポーカー + ダブルアップチャンス）
        """

        self.poker_game()
        # 役ありはダブルアップチャンス
        if self.is_poker_win:
            self.doubleUp_game()


if __name__ == '__main__':
    game = Game()
    game.main()
