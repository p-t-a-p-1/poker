import re


class DoubleUp:

    RANKS = (*"23456789", "10", *"JQKA")
    VALUES = (range(2, 14 + 1))
    # 表示マークとスコアを紐づける
    RANK_TO_VALUES = dict(zip(RANKS, VALUES))

    def __init__(self, deck, player):
        self.deck = deck
        self.player = player
        self.is_game_win = True

    def main_game(self):

        while self.is_game_win:
            print("double-Up Chance Game start")
            print(f"Now, your score is {self.player.score} points.")
            self.player.hands = []

            # デッキから5枚のカードを配る
            self.player.draw_card(self.deck, 5)

            # 5枚中1枚が表、4枚は裏向きでセット
            print(f"player's hands：{self.player.hands[0]}, *-*, *-*, *-*, *-*")

            # カードを1枚ずつ表示して番号を割り振る
            check_hands = []
            for card_idx, card_val in enumerate(self.player.hands):
                # print(f"{card_idx}：{card_val}")
                # 連想配列に追加
                check_card_set = str(card_val).split("-")
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
                # 1番目は選択できない
                if card_idx >= 1:
                    # 隠す
                    # print(f"{card_idx}：*-*")
                    print(f"{card_idx}：{card_val}")

            # 4枚の裏向きカードの中から、表向きのカードの数字より強いものを1枚選ぶ
            card_select_msg = f"Enter a card number that is stronger than {self.player.hands[0]}："
            card_select_res = input(card_select_msg)

            # １〜４までの数字から１つ選ぶ
            if re.compile(r'^[1-4]+$').match(card_select_res) is not None:
                # 選んだ番号のカードと表向きのカードの数字の大きさ比較
                if check_hands[int(card_select_res)]["number"] >= check_hands[0]["number"]:
                    # 大きければスコア２倍
                    print("win!")
                    self.player.score *= 2
                else:
                    # 小さい場合, スコアは0になり、再度ポーカーからスタート
                    print("lose..")
                    self.player.score = 0
                    self.is_game_win = False
            else:
                print("ダメです")

            print(self.player.score)
