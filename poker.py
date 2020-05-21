class Poker:

    RANKS = (*"23456789", "10", *"JQKA")
    VALUES = (range(2, 14 + 1))
    # 表示マークとスコアを紐づける
    RANK_TO_VALUES = dict(zip(RANKS, VALUES))

    def __init__(self, deck, player):
        self.deck = deck
        self.player = player

    def change_hands(self, player_hands):
        check_hands = []

        # それぞれのカードを「のこす」か「かえる」のどちらかを選択
        print("Enter \"y\" to replace the card.")

        for card_idx, change_card in enumerate(player_hands):
            change_card_msg = f"{change_card}："
            change_card_res = input(change_card_msg)

            # 変える場合は山札からドローしてカードを交換
            if change_card_res == "y":
                # デッキからドローして上書き
                change_card = self.deck.pick_card(1)[0]
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
        return check_hands

    def calc_hand(self, check_hands):
        is_flash = True
        # ストレート（数字が連番）
        is_straight = True
        # 同じ数字のカウント
        same_number_count = 0
        same_number = 0
        # ペア数（1ペアや2ペア）
        match_pair_count = 0

        check_hands_sorted = sorted(check_hands, key=lambda x: x["number"])

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
                        same_number = same_number_count + 1

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

        hand_results = {
            "is_flash": is_flash,
            "is_straight": is_straight,
            "same_number_count": same_number_count,
            "same_number": same_number,
            "match_pair_count": match_pair_count
        }
        return hand_results

    def showdown_hand(self, hand_status, check_hands):
        # 結果
        hand_result_msg = ""

        # フラッシュかつストレート
        if hand_status["is_flash"] and hand_status["is_straight"]:
            # 最小のカードが10,最大のカードが14(A)
            if check_hands[0]["number"] == 10 and  \
                    check_hands[4]["number"] == 14:
                hand_result_msg = "ロイヤルストレートフラッシュ"
            else:
                hand_result_msg = "ストレートフラッシュ"

        # 4カード
        elif hand_status["same_number"] == 4:
            hand_result_msg = "4カード"

        # 3カード, フルハウス判定
        elif hand_status["same_number"] == 3:
            # 3カードかつペアが1
            if hand_status["match_pair_count"] == 1:
                hand_result_msg = "フルハウス"
            else:
                hand_result_msg = "3カード"

        # フラッシュ
        elif hand_status["is_flash"]:
            hand_result_msg = "フラッシュ"

        # ストレート
        elif hand_status["is_straight"]:
            hand_result_msg = "ストレート"

        # 2ペア
        elif hand_status["match_pair_count"] == 2:
            hand_result_msg = "2ペア"

        # 1ペア
        elif hand_status["match_pair_count"] == 1:
            hand_result_msg = "1ペア"

        return hand_result_msg

    def main_game(self):
        """
        ポーカー
        """

        print("Poker Game start")

        # 最初は5枚ドロー
        self.player.draw_card(self.deck, 5)

        # 初期カード表示
        print(f"player's hands：{self.player.hands}")

        # カード交換フェイズ
        check_hands = self.change_hands(self.player.hands)

        # 交換後のカード表示
        print(f"player's hands：{self.player.hands}")

        # 手札の数字をもとに昇順にソート
        check_hands_sorted = sorted(check_hands, key=lambda x: x["number"])

        # 役計算のテスト（カード指定）
        # check_hands_sorted = [
        #     {'mark': '♦︎', 'rank': '5', 'number': 5},
        #     {'mark': '❤︎', 'rank': 'J', 'number': 11},
        #     {'mark': '❤︎', 'rank': 'A', 'number': 14},
        #     {'mark': '♣️', 'rank': 'A', 'number': 14},
        #     {'mark': '❤︎', 'rank': 'A', 'number': 14}
        # ]
        # 手札から役の計算
        hand_results = self.calc_hand(check_hands_sorted)
        print(hand_results)
        # 役判定
        hand_result_msg = self.showdown_hand(hand_results, check_hands_sorted)

        # 何もない場合は負け
        if hand_result_msg == "":
            hand_result_msg = "役はありませんでした..."
            self.player.is_poker_win = False

        # 結果出力
        print(hand_result_msg)
