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
        # North
        if direction == 'n':
            newx = self.x - 1
        # South
        elif direction == 's':
            newx = self.x + 1
        # West
        elif direction == 'w':
            newy = self.y - 1
        # East
        elif direction == 'e':
            newy = self.y + 1

        if (newx >= 0) and (newy >= 0) and (newx <= ROWS - 1) and (newy <= COLUMNS - 1):
            self.x = newx
            self.y = newy

        # Agent reached ends
        if self.x == ENDX and self.y == ENDY:
            self.is_agent_reach = True

        # Corrapse
        if self.board[(self.x, self.y)] == -1:
            self.is_agent_die = True

        return (self.x, self.y)

    def reward(self):
        if self.board[(self.x, self.y)] == 0:
            return -1
        if self.board[(self.x, self.y)] == 'E':
            return +100
        else:
            return -100

    def render(self):
        for i in range(0, ROWS):
            for j in range(0, COLUMNS):
                if self.board[i, j] == -1:
                    p = '-1'
                if self.board[i, j] == 0:
                    p = ' 0'
                if i == self.x and j == self.y:
                    p = ' S'
                if i == self.endx and j == self.endy:
                    p = ' E'
                print(p, end='')
            print()






