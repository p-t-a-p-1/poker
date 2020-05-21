class DoubleUp:

    def __init__(self, player):
        self.player = player

    def main_game(self):
        print("double-Up Chance Game start")
        print(f"Now, your score is {self.player.score} points.")

        # TODO デッキから5枚のカードが配られる

        # TODO 5枚中1枚が表、4枚は裏向きでセット

        # TODO 4枚の裏向きカードの中から、表向きのカードの数字より強いものを1枚選ぶ

        # TODO 選択したカードが強い場合, 賭け金は倍になり再度ダブルアップチャンスができる
        # TODO 選択したカードが弱い場合, 賭け金は0になり、再度ポーカーからスタート
