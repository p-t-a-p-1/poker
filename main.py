from deck import stock


class Player:
    """
    メインゲーム（インスタンス作成時にplayerとdealerインスタンス作成）
    """

    def __init__(self):
        self.money = 100
        self.hands = []


class Game:
    """
    メインゲーム（インスタンス作成時にplayerとdealerインスタンス作成）

    Examples
    --------
    >>> game = Game()
    >>> game.main() # ゲームスタート（下記の初期フェーズが表示）

    """

    def __init__(self):
        # player作成
        self.player = Player()

    def main(self):
        """
        ブラックジャックのメインゲーム関数
        """

        # 山札セット（セット数を決める）
        deck = stock.Deck()
        print(deck.cards)
        print(self.player.money)


if __name__ == '__main__':
    game = Game()
    game.main()
