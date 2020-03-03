import copy


def check(l1, l2):
    if l2 not in l1:
        return False
    return True


class TicTacToe:
    def __init__(self):
        self.player = None
        self.board = None
        self.opponent = None
        self.bestMove = None
        self.moveKeys = []
        self.moveValues = []

    def set_board(self, board):
        self.board = board

    def set_player(self, player):
        self.player = player

    def set_opponent(self, opponent):
        self.opponent = opponent

    def evaluate(self, b):
        for row in range(0, 3):
            if b[row][0] == b[row][1] and b[row][1] == b[row][2]:

                if b[row][0] == self.player:
                    return 10
                elif b[row][0] == self.opponent:
                    return -10

        # Checking for Columns for X or O victory.
        for col in range(0, 3):

            if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

                if b[0][col] == self.player:
                    return 10
                elif b[0][col] == self.opponent:
                    return -10
        if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

            if b[0][0] == self.player:
                return 10
            elif b[0][0] == self.opponent:
                return -10

        if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

            if b[0][2] == self.player:
                return 10
            elif b[0][2] == self.opponent:
                return -10
        return 0

    def isFullBoard(self, board):
        for x in board:
            for y in x:
                if y == '':
                    return False
        return True

    def createNewNode(self, currentBoard, nChar, oChar):
        newNode = currentBoard[:]
        c = 0
        for x in currentBoard:
            col = 0
            for y in x:
                if y == oChar:
                    newNode[c][col] = nChar
                    return newNode
                col -= -1
            c -= -1
        return newNode

    def findNumberEmptyTemp(self, board):
        emptySpace = []
        row = 0
        for x in board:
            col = 0
            for y in x:
                if y == '':
                    emptySpace.append([row, col])
                col -= -1
            row -= -1
        return emptySpace

    def findNumberEmpty(self):
        emptySpace = []
        row = 0
        for x in self.board:
            col = 0
            for y in x:
                if y == '':
                    emptySpace.append([row, col])
                col -= -1
            row -= -1
        return emptySpace

    def minimax(self, board, depth, isMax):
        score = self.evaluate(board)
        if depth > 900:
            return 0
        self.depth = depth
        if score == 10:
            return score
        if score == -10:
            return score
        if self.isFullBoard(board):
            return 0
        if isMax:
            eSpaces = self.findNumberEmptyTemp(board)
            best = -999
            for i in eSpaces:
                temp = copy.deepcopy(board)
                temp[i[0]][i[1]] = self.player
                if check(self.moveKeys, temp) == False:
                    self.moveKeys.append(temp)
                    self.moveValues.append(board)
                    nbest = self.minimax(temp, depth+1, not isMax)
                    best = max(best, nbest)
                else:
                    best = 0
                    pass
            return best
        else:
            eSpaces = self.findNumberEmptyTemp(board)
            best = 999
            for i in eSpaces:
                temp = copy.deepcopy(board)
                temp[i[0]][i[1]] = self.opponent
                if check(self.moveKeys, temp) == False:
                    self.moveKeys.append(temp)
                    self.moveValues.append(board)
                    nbest = self.minimax(temp, depth+1, not isMax)
                    best = min(best, nbest)
                else:
                    best = -10
                    pass
            return best

    def findBestMove(self):
        self.bestval = -999
        eSpaces = self.findNumberEmpty()
        bestDepth = 0
        self.keys = []
        self.values = []
        for i in eSpaces:
            nboard = copy.deepcopy(self.board)
            row = i[0]
            col = i[1]
            nboard[row][col] = self.player
            self.values.append(self.board)
            self.keys.append(nboard)
        for x in range(len(self.keys)):

            movVal = self.minimax(self.keys[x], 0, False)
            if movVal > self.bestval:
                self.bestval = movVal
                self.bestMove = eSpaces[x]
                bestDepth = self.depth
            elif movVal == self.bestval:
                if bestDepth > self.depth:
                    self.bestval = movVal
                    self.bestMove = eSpaces[x]
                    bestDepth = self.depth
                else:
                    pass
        return self.bestMove
