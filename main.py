
class Board:

    def __init__(self):
        self.state = [ 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.initialized = False

    def sign_to_printable(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"

    def make_turn(self, cell, player):
        if self.is_valid_turn(cell):
            self.state[cell] = player.symbol
            return True
        else:
            return False

    def is_valid_turn(self, cell):
        if self.state[cell] != 0:
            return False
        else:
            return True

    def check_win(self, player):
        symbol = player.symbol
        if self.state[0] == symbol and self.state[1] == symbol and self.state[2] == symbol:
            return True
        elif self.state[3] == symbol and self.state[4] == symbol and self.state[5] == symbol:
            return True
        elif self.state[6] == symbol and self.state[7] == symbol and self.state[8] == symbol:
            return True
        elif self.state[0] == symbol and self.state[4] == symbol and self.state[8] == symbol:
            return True
        elif self.state[0] == symbol and self.state[3] == symbol and self.state[6] == symbol:
            return True
        elif self.state[1] == symbol and self.state[4] == symbol and self.state[7] == symbol:
            return True
        elif self.state[2] == symbol and self.state[5] == symbol and self.state[8] == symbol:
            return True
        elif self.state[2] == symbol and self.state[4] == symbol and self.state[6] == symbol:
            return True
        else:
            return False

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True

    def print_board(self):
        self.initialized = True
        print(" " + self.sign_to_printable(self.state[0]) + " | " + self.sign_to_printable(self.state[1]) + " | " + self.sign_to_printable(self.state[2]) + "\n"
              + " " + self.sign_to_printable(self.state[3]) + " | " + self.sign_to_printable(self.state[4]) + " | " + self.sign_to_printable(self.state[5]) + "\n"
              + " " + self.sign_to_printable(self.state[6]) + " | " + self.sign_to_printable(self.state[7]) + " | " + self.sign_to_printable(self.state[8]) + "\n")

class Player:

    def __init__(self, symbol):
        self.symbol = symbol

    def set_name(self, name):
        self.name = name

if __name__ == '__main__':
    player1 = Player(1)
    player2 = Player(2)
    board = Board()
    active_player = player1
    if not board.initialized:
        name = input("Choose your name Player 1? \n")
        player1.set_name(name)
        name = input("Choose your name Player 2? \n")
        player2.set_name(name)
    while not board.is_full():

        board.print_board()
        try:
            cell = int(input("Where do you mant to place your sign " + active_player.name + "?\n"))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0  or cell > 8:
            print("Invalid input. Please enter a number between 1 and 9")
            continue
        if not board.make_turn(cell, active_player):
            print("Invalid move.")
            continue
        else:
            if board.check_win(active_player):
                board.print_board()
                print( active_player.name + " won the game! Congratulations!" )
                exit()

        if active_player == player1:
            active_player = player2
        else:
            active_player = player1