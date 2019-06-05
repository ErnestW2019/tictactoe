import board


class Player(object):
    """玩家类"""
    def __init__(self,name):
        self.name = name     # 姓名
        self.score = 0       # 成绩
        self.chess = None    # 棋子

    def move(self,chess_board):
        """在棋盘落子
        ：param chess_board
        """
        # 1 .由用户输入要落子类型
        index = -1
        while index not in chess_board.moveable_list:
            try:
                index = int(input("请 '%s' 输入落子位置 %s:" % (self.name, chess_board.moveable_list)))
            except ValueError:
                pass
        # 2 .在指定位置落子
        chess_board.move_down(index,self.chess)


if __name__ == '__main__':
    # 1 . 创建棋盘对象
    chess_board = board.Board()
    # 2 . 创建玩家对象
    human = Player("玩家")
    human.chess = "X"
    # 3. 玩家在棋盘上循环落子，直到玩家胜利
    while not chess_board.is_win(human.chess):
        human.move(chess_board)
        # 显示棋盘
        chess_board.show_board()

