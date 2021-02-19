from enum import Enum



class TicTacToe:
    # Basic enum class for reference later
    class STATES(Enum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    # Initiating blank board with cross turn
    def __init__(self):
        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.curr_state = 0
        self.tiles_filled = 0

    # Helper function to print turn and board for game user
    def print_status(self):
        print(self.STATES(self.curr_state).name) # Status above board
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])

    # place_marker takes in a symbol, row, and column for
    # the proposed move, and changes the board state, then
    # returns the board_state at the end of the move.
    def place_marker(self, symbol, row, column):
        if symbol != "x" and symbol != "o": # Not an x or o
            return "Not a valid symbol!"
        if row < 0 or row > 2 or column < 0 or column > 2: # Not within bounds
            return "Not a valid tile!"
        if self.board[row][column] != "-": # Board tile already used
            return "Already filled!"
        if self.curr_state == 0 and symbol == "o": # Both wrong turn checkers
            return "Wrong turn!"
        if self.curr_state == 1 and symbol == "x":
            return "Wrong turn!"

        # Populates board with new symbol and increases counter
        self.board[row][column] = symbol
        self.tiles_filled += 1

        # Uses check_state helper function to get new state for board
        new_state = self.check_state(symbol, row, column)

        # If state is greater than 1, game ends and is reset.
        if new_state > 1:
            self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]
            self.curr_state = 0
            self.tiles_filled = 0

        # Returns end state of the specified move
        return self.STATES(new_state)

    # check_state finds and returns the new state of a post-move board
    def check_state(self, symbol, row, column):
        # Can only win after own turn, so saves computation to only check
        # x or o at their own turn, in their own row and column
        if symbol == "x":
            if self.board[row] == ["x","x","x"]: # Row check
                return 3 # CROSS_WON
            elif self.board[0][column] == "x" and self.board[1][column] == "x" \
                and self.board[2][column] == "x": # Column check
                return 3
            # Diagonals not worth checking if a new placement is in diagonal
            elif self.board[0][0] == "x" and self.board[1][1] == "x" \
                and self.board[2][2] == "x":
                return 3
            elif self.board[0][2] == "x" and self.board[1][1] == "x" \
                and self.board[2][0] == "x":
                return 3

        # Same as above for o
        if symbol == "o":
            if self.board[row] == ["o","o","o"]:
                return 4 # NAUGHT_WON
            elif self.board[0][column] == "o" and self.board[1][column] == "o" \
                and self.board[2][column] == "o":
                return 4
            elif self.board[0][0] == "o" and self.board[1][1] == "o" \
                and self.board[2][2] == "o":
                return 4
            elif self.board[0][2] == "o" and self.board[1][1] == "o" \
                and self.board[2][0] == "o":
                return 4
        
        
        if self.tiles_filled == 9: # If board filled, and win was not triggered, draw
            return 2 # DRAW
        elif self.curr_state == 0: # Flips turn state from x to o
            self.curr_state = 1 # NAUGHT_TURN
            return 1
        else: # Flips turn state from o to x
            self.curr_state = 0 # CROSS_TURN
            return 0 



# Basic implementation of command line gameplay
if __name__ == '__main__':
    print("Welcome to TicTacToe! Type QUIT to quit.")
    print("When prompted, enter row and column seperated by a space, like \"0 2\"")
    board = TicTacToe()
    board.print_status()
    while (1):
        new_input = input("Input coordinates: ")
        if new_input == "QUIT":
            exit()
        sep = new_input.split()
        row, column = int(sep[0]), int(sep[1])
        if board.curr_state == 0:
            next_status = board.place_marker("x", row, column)
        elif board.curr_state == 1:
            next_status = board.place_marker("o", row, column)
        if next_status.value > 1:
            print("Game ended:", next_status.name)
            print("\nRestarting...\n")
        board.print_status()
    exit()