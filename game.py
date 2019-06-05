import board
import player
import random


class Game(object):
    """游戏类"""
    def __init__(self):
        self.chess_board = board.Board()  # 棋盘对象
        self.human = player.Player("玩家1")      # 人类玩家对象1
        self.computer = player.Player("玩家2")  # 人类玩家对象2

    def random_player(self):
        """随机先手玩家
        ：return:落子先后顺序的玩家数组
        """
        # 如果产生随机数为1 表示玩家先手
        if random.randint(0,1) == 1:
            players = (self.human, self.computer)
        else:
            players = (self.computer, self.human)
        # 设置玩家棋子
        players[0].chess = "X"
        players[1].chess = "O"
        print("根据随机抽取结果 %s 先行" % players[0].name)
        return players


    def play_round(self):
        """一轮完整的对局"""
        # 1. 显示棋盘落子位置
        self.chess_board.show_board(True)
        # 2 .随机决定先手
        current_player, next_player = self.random_player()
        # 3 .两个玩家轮流落子
        while True:
            # 落子方落子
            current_player.move(self.chess_board)
            # 显示落子结果
            self.chess_board.show_board()
            # 是否胜利？
            if self.chess_board.is_win(current_player.chess):
                print("%s 战胜 %s" %(current_player.name, next_player.name))
                current_player.score += 1
                break
            # 是否平局？
            if self.chess_board.is_draw():
                print("%s 和 %s 战成平局" % (current_player.name, next_player.name))
                break
            # 交换落子方
            current_player, next_player = next_player, current_player
        # 4. 显示比分
        print("[%s] 对战 [%s] 比分是 %d : %d" % (self.human.name, self.computer.name, self.human.score, self.computer.score))


if __name__ == '__main__':
    Game().play_round()
