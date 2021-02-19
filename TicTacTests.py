import unittest
from TicTacToe import *


class TicTacTest(unittest.TestCase):

    # Tests for input errors, which all return strings specifying the problem
    def test_input(self):
        curr_board = TicTacToe()
        # Tests for any symbol that is not an x or o
        self.assertEqual("Not a valid symbol!", curr_board.place_marker("a", 0, 0)) 
        # Tests for wrong tile in row
        self.assertEqual("Not a valid tile!", curr_board.place_marker("x", 0, 4))  
        # Tests for wrong tile in column 
        self.assertEqual("Not a valid tile!", curr_board.place_marker("x", 4, 0))  
        # Populates tile, then checks to not fill it again 
        self.assertEqual(TicTacToe.STATES(1), curr_board.place_marker("x", 0, 0))
        self.assertEqual("Already filled!", curr_board.place_marker("o", 0, 0))
        # Tests for inputting opposite symbol on wrong turn
        self.assertEqual("Wrong turn!", curr_board.place_marker("x", 0, 1))
        self.assertEqual(TicTacToe.STATES(0), curr_board.place_marker("o", 0, 1))
        self.assertEqual("Wrong turn!", curr_board.place_marker("o", 1, 0))

    '''
    For all further tests, it is feasible that more tests could be created to
    test a solution in each possible row or column to win on, but the way
    the solution is implemented only checks the row and column the move
    was just done on in the first place, and there is no functional difference
    between any individual row or column in a solution.
    '''
    def test_horizontal(self):
        horiz_board = TicTacToe()
        # Testing that cross is able to win the game horizontally
        self.assertEqual(TicTacToe.STATES(1), horiz_board.place_marker("x", 0, 0))
        self.assertEqual(TicTacToe.STATES(0), horiz_board.place_marker("o", 1, 0))
        self.assertEqual(TicTacToe.STATES(1), horiz_board.place_marker("x", 0, 1))
        self.assertEqual(TicTacToe.STATES(0), horiz_board.place_marker("o", 1, 1))
        self.assertEqual(TicTacToe.STATES(3), horiz_board.place_marker("x", 0, 2))
        # Testing that naught is able to win the game horizontally
        self.assertEqual(TicTacToe.STATES(1), horiz_board.place_marker("x", 0, 0))
        self.assertEqual(TicTacToe.STATES(0), horiz_board.place_marker("o", 1, 0))
        self.assertEqual(TicTacToe.STATES(1), horiz_board.place_marker("x", 0, 1))
        self.assertEqual(TicTacToe.STATES(0), horiz_board.place_marker("o", 1, 1))
        self.assertEqual(TicTacToe.STATES(1), horiz_board.place_marker("x", 2, 0))
        self.assertEqual(TicTacToe.STATES(4), horiz_board.place_marker("o", 1, 2))

    def test_vertical(self):
        vert_board = TicTacToe()
        # Testing that cross is able to win the game vertically
        self.assertEqual(TicTacToe.STATES(1), vert_board.place_marker("x", 0, 0))
        self.assertEqual(TicTacToe.STATES(0), vert_board.place_marker("o", 0, 1))
        self.assertEqual(TicTacToe.STATES(1), vert_board.place_marker("x", 1, 0))
        self.assertEqual(TicTacToe.STATES(0), vert_board.place_marker("o", 1, 1))
        self.assertEqual(TicTacToe.STATES(3), vert_board.place_marker("x", 2, 0))
        # Testing that naught is able to win the game vertically
        self.assertEqual(TicTacToe.STATES(1), vert_board.place_marker("x", 0, 0))
        self.assertEqual(TicTacToe.STATES(0), vert_board.place_marker("o", 0, 2))
        self.assertEqual(TicTacToe.STATES(1), vert_board.place_marker("x", 1, 0))
        self.assertEqual(TicTacToe.STATES(0), vert_board.place_marker("o", 1, 2))
        self.assertEqual(TicTacToe.STATES(1), vert_board.place_marker("x", 0, 1))
        self.assertEqual(TicTacToe.STATES(4), vert_board.place_marker("o", 2, 2))

    # Testing diagonal victory in forward direction (like forward slash)
    def test_diagonal_forward(self):
        diag_board = TicTacToe()
        # Testing that cross is able to win the game diagonally
        self.assertEqual(TicTacToe.STATES(1), diag_board.place_marker("x", 0, 2))
        self.assertEqual(TicTacToe.STATES(0), diag_board.place_marker("o", 1, 0))
        self.assertEqual(TicTacToe.STATES(1), diag_board.place_marker("x", 1, 1))
        self.assertEqual(TicTacToe.STATES(0), diag_board.place_marker("o", 0, 1))
        self.assertEqual(TicTacToe.STATES(3), diag_board.place_marker("x", 2, 0))
        # Testing that naught is able to win the game diagonally
        self.assertEqual(TicTacToe.STATES(1), diag_board.place_marker("x", 1, 0))
        self.assertEqual(TicTacToe.STATES(0), diag_board.place_marker("o", 0, 2))
        self.assertEqual(TicTacToe.STATES(1), diag_board.place_marker("x", 0, 1))
        self.assertEqual(TicTacToe.STATES(0), diag_board.place_marker("o", 1, 1))
        self.assertEqual(TicTacToe.STATES(1), diag_board.place_marker("x", 2, 2))
        self.assertEqual(TicTacToe.STATES(4), diag_board.place_marker("o", 2, 0))

    # Testing diagonal victory in backwards direction (like backslash)
    def test_diagonal_backward(self):
        diag_board = TicTacToe()
        # Testing that cross is able to win the game diagonally
        self.assertEqual(TicTacToe.STATES(1), diag_board.place_marker("x", 0, 0))
        self.assertEqual(TicTacToe.STATES(0), diag_board.place_marker("o", 1, 0))
        self.assertEqual(TicTacToe.STATES(1), diag_board.place_marker("x", 1, 1))
        self.assertEqual(TicTacToe.STATES(0), diag_board.place_marker("o", 0, 1))
        self.assertEqual(TicTacToe.STATES(3), diag_board.place_marker("x", 2, 2))
        # Testing that naught is able to win the game diagonally
        self.assertEqual(TicTacToe.STATES(1), diag_board.place_marker("x", 1, 0))
        self.assertEqual(TicTacToe.STATES(0), diag_board.place_marker("o", 0, 0))
        self.assertEqual(TicTacToe.STATES(1), diag_board.place_marker("x", 0, 1))
        self.assertEqual(TicTacToe.STATES(0), diag_board.place_marker("o", 1, 1))
        self.assertEqual(TicTacToe.STATES(1), diag_board.place_marker("x", 2, 0))
        self.assertEqual(TicTacToe.STATES(4), diag_board.place_marker("o", 2, 2))

    # Testing to create a draw
    def test_draw(self):
        draw_board = TicTacToe()
        # Draws can only end with a cross, so only one set needed
        self.assertEqual(TicTacToe.STATES(1), draw_board.place_marker("x", 0, 0))
        self.assertEqual(TicTacToe.STATES(0), draw_board.place_marker("o", 1, 1))
        self.assertEqual(TicTacToe.STATES(1), draw_board.place_marker("x", 0, 2))
        self.assertEqual(TicTacToe.STATES(0), draw_board.place_marker("o", 0, 1))
        self.assertEqual(TicTacToe.STATES(1), draw_board.place_marker("x", 2, 1))
        self.assertEqual(TicTacToe.STATES(0), draw_board.place_marker("o", 1, 2))
        self.assertEqual(TicTacToe.STATES(1), draw_board.place_marker("x", 1, 0))
        self.assertEqual(TicTacToe.STATES(0), draw_board.place_marker("o", 2, 0))
        self.assertEqual(TicTacToe.STATES(2), draw_board.place_marker("x", 2, 2))

    # Testing to create a draw, then reset the board properly
    def test_reset(self):
        reset_board = TicTacToe()
        # Creating draw to fill board
        self.assertEqual(TicTacToe.STATES(1), reset_board.place_marker("x", 0, 0))
        self.assertEqual(TicTacToe.STATES(0), reset_board.place_marker("o", 1, 1))
        self.assertEqual(TicTacToe.STATES(1), reset_board.place_marker("x", 0, 2))
        self.assertEqual(TicTacToe.STATES(0), reset_board.place_marker("o", 0, 1))
        self.assertEqual(TicTacToe.STATES(1), reset_board.place_marker("x", 2, 1))
        self.assertEqual(TicTacToe.STATES(0), reset_board.place_marker("o", 1, 2))
        self.assertEqual(TicTacToe.STATES(1), reset_board.place_marker("x", 1, 0))
        self.assertEqual(TicTacToe.STATES(0), reset_board.place_marker("o", 2, 0))
        self.assertEqual(TicTacToe.STATES(2), reset_board.place_marker("x", 2, 2))
        # Checking variables and game state after draw
        self.assertEqual([["-","-","-"],["-","-","-"],["-","-","-"]], reset_board.board)
        self.assertEqual(0, reset_board.tiles_filled)
        self.assertEqual(0, reset_board.curr_state)
        self.assertEqual(TicTacToe.STATES(1), reset_board.place_marker("x", 0, 0))