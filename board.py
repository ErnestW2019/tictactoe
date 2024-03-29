class Board(object):
    """棋盘类"""
    def __init__(self):
        self.board_data = [" "] * 9     # 棋盘数据
        self.moveable_list = list(range(9))  # 可移动列表

    def show_board(self,show_index=False):
        """显示棋盘
        :param show_index:True  表示显示索引 / False 表示显示数据
        """
        for i in (0,3,6):
            print("         |         |")
            if show_index:
                print("    %d    |    %d    |    %d" % (i,i + 1, i + 2))
            else:
                print("    %s    |    %s    |    %s" %(self.board_data[i],
                                                            self.board_data[i + 1],
                                                            self.board_data[i + 2]))
            print("         |         |")
            if i != 6:
                print("-" * 30)

    def move_down(self,index,chess):
        """在指定位置落子
        :param index:列表索引
        :param chess:棋子类型 ×或 0
        """
        # 1. 判断  index  是否在可移动列表中
        if index not in self.moveable_list:
            print("%d 位置不允许落子" % index)
            return
        # 2.修改棋盘数据
        self.board_data[index] = chess
        # 3.修改可移动列表
        self.moveable_list.remove(index)

    def is_draw(self):
        """是否平局"""
        return len(self.moveable_list) == 0

    def is_win(self,chess):
        """是否胜利
        :param chess:玩家的棋子
        """
        # 1.定义检查方向列表
        check_dirs = [[0,1,2],[3,4,5],[6,7,8],
                      [0,3,6],[1,4,7],[2,5,8],
                      [0,4,8],[2,4,6]]
        # 2.复制棋盘数据 - 后续 AI 需要使用
        data = self.board_data.copy()
        # 3.遍历检查方向列表判断是否胜利
        for item in check_dirs:
            if (data[item[0]] == chess
                    and data[item[1]] == chess
                    and data[item[2]] == chess):
                return True
        return False

    def reset_board(self):
        """重置棋盘"""
        # 1.清空可移动列表数据
        self.moveable_list.clear()
        # 2.重置数据
        for i in range(9):
            self.board_data[i] = " "
            self.moveable_list.append(i)


if __name__ == '__main__':
    # 1.测试代码初始化
    board = Board()
    print(board.board_data)
    print(board.moveable_list)

    # 2.显示棋盘
    print("___显示棋盘" + "-" * 50)
    board.show_board(True)   # 显示索引
    print("-" * 50)
    board.show_board()  # 显示数据

    # 3.测试落子
    print("--- 测试落子" + "-" * 50)
    board.move_down(0,"X")
    board.show_board()
    print(board.moveable_list)
    board.move_down(0, "X")
    """
    # 4.判断平局
    print("---判断平局" + "-" * 50)
    print("是否平局 %d" % board.is_draw())
    board.moveable_list.clear()    # 清空可移动索引列表
    print("是否平局 %d" % board.is_draw())
    """

    # 5.判断胜利
    print("---判断胜利" + "-" *  50)
    print("是否胜利 %d" % board.is_win("X"))
    board.move_down(0,"X")
    board.move_down(1, "X")
    board.move_down(2, "X")
    board.show_board()
    print("是否胜利 %d" % board.is_win("X"))

    # 6.测试重置棋盘数据
    print("--- 重置棋盘" + "-" * 50)
    board.reset_board()
    board.show_board()
    print(board.moveable_list)
