import numpy as np           # 提供维度数组与矩阵运算
import copy                  # 从copy模块导入深度拷贝方法
from board import Chessboard

# 基于棋盘类，设计搜索策略
class Game:
    def __init__(self, show = True):
        """
        初始化游戏状态.
        """

        self.chessBoard = Chessboard(show)
        self.solves = []
        self.queen = np.zeros((8,8),dtype=np.int8)
        self.gameInit()

    # 重置游戏
    def gameInit(self, show = True):
        """
        重置棋盘.
        """

        self.Queen_setRow = [-1] * 8
        self.chessBoard.boardInit(False)

    ##############################################################################
    ####                请在以下区域中作答(可自由添加自定义函数)                 ####
    ####              输出：self.solves = 八皇后所有序列解的list                ####
    ####             如:[[0,6,4,7,1,3,5,2],]代表八皇后的一个解为                ####
    ####           (0,0),(1,6),(2,4),(3,7),(4,1),(5,3),(6,5),(7,2)            ####
    ##############################################################################
    #                                                                            #
    def check(self, x, y):
        for i in range(x):
            if self.queen[i][y] == 1:
                return False
        for i, j in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
            if self.queen[i][j] == 1:
                return False
        for i, j in zip(range(x - 1, -1, -1), range(y + 1, 8)):
            if self.queen[i][j] == 1:
                return False
        return True

    def dfs(self, row=0):
        if row > 7:
            self.solves.append(copy.deepcopy(self.Queen_setRow))
            return
        for col in range(8):
            if self.check(row, col):
                self.queen[row][col] = 1
                self.Queen_setRow[row] = col
                self.dfs(row + 1)
                self.queen[row][col] = 0

    def run(self, row=0):
        self.dfs(0)
        # self.solves.append([0,6,4,7,1,3,5,2])

    #                                                                            #
    ##############################################################################
    #################             完成后请记得提交作业             #################
    ##############################################################################

    def showResults(self, result):
        """
        结果展示.
        """

        self.chessBoard.boardInit(False)
        for i,item in enumerate(result):
            if item >= 0:
                self.chessBoard.setQueen(i,item,False)

        self.chessBoard.printChessboard(False)

    def get_results(self):
        """
        输出结果(请勿修改此函数).
        return: 八皇后的序列解的list.
        """

        self.run()
        return self.solves


game = Game()
solutions = game.get_results()
print('There are {} results.'.format(len(solutions)))
game.showResults(solutions[0])