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

    RANKS = (*"23456789", "10", *"JQKA")
    VALUES = (range(2, 14 + 1))
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

        # チェック用のカードリスト（mark, rank, number）
        check_hands = []

        # TODO Pokerクラスにメソッド追加
        # change_hands
        # カード交換、チェック用のカードリストに追加
        for card_idx, change_card in enumerate(self.player.hands):
            change_card_msg = f"{change_card}："
            change_card_res = input(change_card_msg)

            # 変える場合は山札からドローしてカードを交換
            if change_card_res == "y":
                # デッキからドローして上書き
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

        # TODO Pokerクラスにメソッド追加
        # calc_poker_hand
        # 役の確認
        # フラッシュ（マーク全て一致）
        is_flash = True
        # ストレート（数字が連番）
        is_straight = True
        # 同じ数字のカウント
        same_number_count = 0
        same_number = 0
        # ペア数（1ペアや2ペア）
        match_pair_count = 0

        # check_hands_sorted = [
        #     {'mark': '♣️', 'rank': '3', 'number': 3},
        #     {'mark': '♠︎', 'rank': '3', 'number': 3},
        #     {'mark': '♣️', 'rank': '3', 'number': 3},
        #     {'mark': '♠︎', 'rank': '3', 'number': 3},
        #     {'mark': '♣️', 'rank': '6', 'number': 6}
        # ]

        for check_idx, check_card in enumerate(check_hands_sorted):

            # 1枚目は前のカードがないのでスキップ
            if check_idx == 0:
                continue

            # 前のカード {'mark': '♠︎', 'rank': '4', 'number': 4}
            prev_card = check_hands_sorted[check_idx - 1]

            # 前後のマーク違う場合はフラッシュ判定をFalse
            if is_flash and check_card["mark"] != prev_card["mark"]:
                is_flash = False

            # 前後で数字が連続していない場合はストレート判定をFalse
            if is_straight and check_card["number"] != prev_card["number"] + 1:
                is_straight = False

            # 前後で数字が一致してる場合は 同じ数字のカウント を+1
            if check_card["number"] == prev_card["number"]:
                # マッチ数 + 1
                same_number_count += 1

                # 最後のカード
                if check_idx == 4:
                    if same_number_count == 1:
                        # ペア数 + 1
                        match_pair_count += 1
                    else:
                        # 3カードや4カード
                        same_number = match_pair_count + 1

            # 違う数字の場合
            else:
                if same_number_count == 1:
                    # ペア数 + 1
                    match_pair_count += 1
                elif same_number_count > 1:
                    # 3カードや4カード
                    same_number = same_number_count + 1
                # 違う数字なのでリセット
                same_number_count = 0

        # TODO Pokerクラスにメソッド追加
        # check_poker_hand

        # 役判定
        hand_result_msg = ""

        # フラッシュかつストレート
        if is_flash and is_straight:
            # 最小のカードが10,最大のカードが14(A)
            if check_hands_sorted[0]["number"] == 10 and  \
                    check_hands_sorted[4]["number"] == 14:
                hand_result_msg = "ロイヤルストレートフラッシュ"
            else:
                hand_result_msg = "ストレートフラッシュ"

        # 4カード
        elif same_number == 4:
            hand_result_msg = "4カード"

        # 3カード, フルハウス判定
        elif same_number == 3:
            # 3カードかつペアが1
            if match_pair_count == 1:
                hand_result_msg = "フルハウス"
            else:
                hand_result_msg = "3カード"

        # フラッシュ
        elif is_flash:
            hand_result_msg = "フラッシュ"

        # ストレート
        elif is_straight:
            hand_result_msg = "ストレート"

        # 2ペア
        elif match_pair_count == 2:
            hand_result_msg = "2ペア"

        # 1ペア
        elif match_pair_count == 1:
            hand_result_msg = "1ペア"

        # 何もない場合は負け
        if hand_result_msg == "":
            hand_result_msg = "no"

        print(hand_result_msg)
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
