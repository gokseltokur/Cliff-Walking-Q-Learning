import numpy as np

ROWS = 4
COLUMNS = 12

STARTX = 3
STARTY = 0

ENDX = 3
ENDY = 11


class Board:
    def __init__(self):
        self.board = np.zeros([ROWS, COLUMNS])
        self.x = STARTX
        self.y = STARTY
        self.startx = STARTX
        self.starty = STARTY
        self.endx = ENDX
        self.endy = ENDY
        self.is_agent_reach = False
        self.is_agent_die = False

        self.board[3][1] = -1
        self.board[3][2] = -1
        self.board[3][3] = -1
        self.board[3][4] = -1
        self.board[3][5] = -1
        self.board[3][6] = -1
        self.board[3][7] = -1
        self.board[3][8] = -1
        self.board[3][9] = -1
        self.board[3][10] = -1

    def move(self, direction):
        newx = None
        newy = None
        # North
        if direction == "n":
            newx = self.x - 1
            newy = self.y
        # South
        elif direction == "s":
            newx = self.x + 1
            newy = self.y
        # West
        elif direction == "w":
            newx = self.x
            newy = self.y - 1
        # East
        elif direction == "e":
            newx = self.x
            newy = self.y + 1

        if (newx >= 0) and (newy >= 0) and (newx <= ROWS - 1) and (newy <= COLUMNS - 1):
            self.x = newx
            self.y = newy

        # Agent reached ends
        if self.x == ENDX and self.y == ENDY:
            self.is_agent_reach = True
            print("Agent reached ends")

        # Corrapse
        if self.board[(self.x, self.y)] == -1:
            self.is_agent_die = True
            print("Agent died")

        return (self.x, self.y)

    def reward(self):
        pos = (self.x, self.y)
        #print(self.x, self.y)
        #print('@' + str(pos))
        if self.x == STARTX and self.y == STARTY :
            return -1
        if self.board[pos] == 0:
            return -1
        if self.board[pos] == 'E':
            return +100
        return -100






