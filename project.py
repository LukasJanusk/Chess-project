board = [
    {"p": "a8", "c": (0, 0)}, {"p": "a7", "c": (0, 1)},
    {"p": "a6", "c": (0, 2)}, {"p": "a5", "c": (0, 3)},
    {"p": "a4", "c": (0, 4)}, {"p": "a3", "c": (0, 5)},
    {"p": "a2", "c": (0, 6)}, {"p": "a1", "c": (0, 7)},
    {"p": "b8", "c": (1, 0)}, {"p": "b7", "c": (1, 1)},
    {"p": "b6", "c": (1, 2)}, {"p": "b5", "c": (1, 3)},
    {"p": "b4", "c": (1, 4)}, {"p": "b3", "c": (1, 5)},
    {"p": "b2", "c": (1, 6)}, {"p": "b1", "c": (1, 7)},
    {"p": "c8", "c": (2, 0)}, {"p": "c7", "c": (2, 1)},
    {"p": "c6", "c": (2, 2)}, {"p": "c5", "c": (2, 3)},
    {"p": "c4", "c": (2, 4)}, {"p": "c3", "c": (2, 5)},
    {"p": "c2", "c": (2, 6)}, {"p": "c1", "c": (2, 7)},
    {"p": "d8", "c": (3, 0)}, {"p": "d7", "c": (3, 1)},
    {"p": "d6", "c": (3, 2)}, {"p": "d5", "c": (3, 3)},
    {"p": "d4", "c": (3, 4)}, {"p": "d3", "c": (3, 5)},
    {"p": "d2", "c": (3, 6)}, {"p": "d1", "c": (3, 7)},
    {"p": "e8", "c": (4, 0)}, {"p": "e7", "c": (4, 1)},
    {"p": "e6", "c": (4, 2)}, {"p": "e5", "c": (4, 3)},
    {"p": "e4", "c": (4, 4)}, {"p": "e3", "c": (4, 5)},
    {"p": "e2", "c": (4, 6)}, {"p": "e1", "c": (4, 7)},
    {"p": "f8", "c": (5, 0)}, {"p": "f7", "c": (5, 1)},
    {"p": "f6", "c": (5, 2)}, {"p": "f5", "c": (5, 3)},
    {"p": "f4", "c": (5, 4)}, {"p": "f3", "c": (5, 5)},
    {"p": "f2", "c": (5, 6)}, {"p": "f1", "c": (5, 7)},
    {"p": "g8", "c": (6, 0)}, {"p": "g7", "c": (6, 1)},
    {"p": "g6", "c": (6, 2)}, {"p": "g5", "c": (6, 3)},
    {"p": "g4", "c": (6, 4)}, {"p": "g3", "c": (6, 5)},
    {"p": "g2", "c": (6, 6)}, {"p": "g1", "c": (6, 7)},
    {"p": "h8", "c": (7, 0)}, {"p": "h7", "c": (7, 1)},
    {"p": "h6", "c": (7, 2)}, {"p": "h5", "c": (7, 3)},
    {"p": "h4", "c": (7, 4)}, {"p": "h3", "c": (7, 5)},
    {"p": "h2", "c": (7, 6)}, {"p": "h1", "c": (7, 7)}
]
white_pieces = [
    {"piece": "pawn", "symbol": "♙"},
    {"piece": "rook", "symbol": "♖"}
]
black_pieces = [
    {"piece": "king", "symbol": "♚"},
    {"piece": "queen", "symbol": "♛"},
    {"piece": "rook", "symbol": "♜"},
    {"piece": "bishop", "symbol": "♝"},
    {"piece": "knight", "symbol": "♞"},
    {"piece": "pawn", "symbol": "♟︎"}
]
white_pieces_on_board = []
black_pieces_on_board = []


def main():
    instructions()
    choose_white_phase()
    choose_black_phase()
    taking_phase()
    print("Game over")


def instructions():
    print_board(8, white_pieces_on_board, black_pieces_on_board)
    print("Choose one white piece either a pawn or a rook then place it on board (e.g. pawn a4).")
    print("Once you have placed white piece you can place from 1 to 16 black pieces.")
    print('When finished placing your pieces type: "done". Program then will check which black pieces can be taken')


def choose_white_phase():
    while True:
        user_input = input("Place white piece: ")
        if check_if_typo_white(user_input):
            print("Invalid input, please place white piece in format e.g. pawn a1")
            continue
        break
    sort_pieces(user_input, white_pieces, white_pieces_on_board)


def choose_black_phase():
    n = 0
    while n < 16:
        user_input = input("Place black piece: ")
        if user_input == "done":
            if check_if_enough_black_pieces_on_board():
                break
            print("Not enough black pieces on the board ")
            continue
        if check_if_typo_black(user_input):
            print(
                "Invalid input, please place chess piece in the correct format e.g. pawn a1 or type: done")
            continue
        if check_if_occupied(user_input):
            print("Square is taken, choose different square")
            continue
        else:
            sort_pieces(user_input, black_pieces, black_pieces_on_board)
            n += 1
            remaining = 16 - n
            print(f"Remaining black pieces: {remaining}")
    while n == 16:
        print("All black pieces have been placed.")
        user_inp = input('Please type "done" to finish: ')
        if user_inp == "done":
            break
        else:
            continue


def taking_phase():
    white_piece = white_pieces_on_board[0]["piece"]
    white_pos = white_pieces_on_board[0]["c"]
    if white_piece == "rook":
        rook_take(white_pos)
    else:
        white_piece == "pawn"
        pawn_take(white_pos)


def check_if_typo_white(text):
    if not text.startswith(("pawn ", "rook ")) or \
            text[-2] not in 'abcdefgh' or text[-1] not in '12345678':
        return True


def check_if_occupied(text):
    cor = text[-2:]
    if check_if_occupied_set(
            cor,
            white_pieces_on_board) or check_if_occupied_set(
            cor,
            black_pieces_on_board):
        return True
    return False


def check_if_occupied_set(cor, pieces_on_board_set):
    for pos in pieces_on_board_set:
        if pos["p"] == cor:
            return True
        return False


def check_if_typo_black(text):
    if not text.startswith(("pawn ", "rook ", "king ", "queen ", "bishop ", "knight ")
                           ) or text[-2] not in 'abcdefgh' or text[-1] not in '12345678':
        return True


def check_if_enough_black_pieces_on_board():
    if 0 < len(black_pieces_on_board) <= 16 and len(
            black_pieces_on_board) != 0:
        return True
    return False


def print_board(size, white_pieces_on_board, black_pieces_on_board):
    for y in range(size):
        print(size - y, end=' ')
        for x in range(size):
            position = (x, y)
            symbol = None
            for cord in white_pieces_on_board:
                if cord["c"] == position:
                    symbol = cord["symbol"]
                    break
            if not symbol:
                for cord in black_pieces_on_board:
                    if cord["c"] == position:
                        symbol = cord["symbol"]
                        break
            if symbol:
                print(symbol, end=' ')
            elif (x + y) % 2 == 0:
                print("▢", end=' ')
            else:
                print("◼", end=' ')
        print()
    print("  a b c d e f g h")


def pawn_take(white_pos):
    x, y = white_pos
    can_take = False
    for black_piece in black_pieces_on_board:
        black_pos = black_piece["c"]
        a, b = black_pos
        if (x + 1, y - 1) == (a, b) or (x - 1, y - 1) == (a, b):
            print(
                "White pawn can take black",
                black_piece["piece"],
                "on",
                black_piece["p"],
                "square")
            can_take = True
    if not can_take:
        print("White pawn cannot take any black pieces")


def rook_take(white_pos):

    def take_right(white_pos):
        x, y = white_pos
        for increment in range(8):
            x_check = x + (increment + 1)
            if not 0 <= x_check <= 7:
                return False
            for pos in black_pieces_on_board:
                position_to_check = (x_check, y)
                black_piece_position = pos["c"]
                if black_piece_position == position_to_check:
                    print(
                        "Rook can take black",
                        pos["piece"],
                        "on",
                        pos["p"],
                        "square")
                    return True
        return False

    def take_left(white_pos):
        x, y = white_pos
        for increment in range(8):
            x_check = x - (increment + 1)
            if not 0 <= x_check <= 7:
                return False
            for pos in black_pieces_on_board:
                position_to_check = (x_check, y)
                black_piece_position = pos["c"]
                if black_piece_position == position_to_check:
                    print(
                        "Rook can take black",
                        pos["piece"],
                        "on",
                        pos["p"],
                        "square")
                    return True
        return False

    def take_down(white_pos):
        x, y = white_pos
        for increment in range(8):
            y_check = y + (increment + 1)
            if not 0 <= y_check <= 7:
                return False
            for pos in black_pieces_on_board:
                position_to_check = (x, y_check)
                black_piece_position = pos["c"]
                if black_piece_position == position_to_check:
                    print(
                        "Rook can take black",
                        pos["piece"],
                        "on",
                        pos["p"],
                        "square")
                    return True
        return False

    def take_up(white_pos):
        x, y = white_pos
        for increment in range(8):
            y_check = y - (increment + 1)
            if not 0 <= y_check <= 7:
                return False
            for pos in black_pieces_on_board:
                position_to_check = (x, y_check)
                black_piece_position = pos["c"]
                if black_piece_position == position_to_check:
                    print(
                        "Rook can take black",
                        pos["piece"],
                        "on",
                        pos["p"],
                        "square")
                    return True
        return False
    check_up = take_up(white_pos)
    check_down = take_down(white_pos)
    check_right = take_right(white_pos)
    check_left = take_left(white_pos)
    if not check_up and not check_down and not check_right and not check_left:
        print("Rook cannot take any black pieces.")


def sort_pieces(user_input, pieces_set, pieces_on_board_set):
    parts = user_input.split()
    piece, position = parts
    if len(white_pieces_on_board) == 1:
        color = "Black"
    else:
        color = "White"
    for figure in pieces_set:
        if figure["piece"] == piece:
            for square in board:
                if square["p"] == position:
                    temp_dict = {
                        "piece": figure["piece"],
                        "symbol": figure["symbol"],
                        "p": square["p"],
                        "c": square["c"]
                    }
                    break
            break
    pieces_on_board_set.append(temp_dict)
    print_board(8, white_pieces_on_board, black_pieces_on_board)
    print(f"{color} {piece} placed on {position} square")


if __name__ == "__main__":
    main()

"""
The exact criteria you are given to implement are as follows:

The program should first ask the user to input a chess piece and where it
is on the board. This will be the white piece. The user should be informed
that they can choose between two pieces of your choice (e.g. pawn and rook).
The choice should be made by writing the piece and the coordinates in a
predefined format in the console, e.g.: knight a5.

Once the user successfully adds the white piece, the user is asked to enter
the black pieces, one by one, in the same format as the white piece.
They need to add at least 1 black piece or 16 at most.
Once at least one black piece has been added, the user can write “done”
instead of the coordinates to add no more pieces.

You can assume that the user will input either “done” or the correct format
for adding a piece (“piece coordinates”).
You can also assume that coordinates will always be entered as where letters
are a-h and digits are 1-8, e.g. a1, d4, h8.
You should not assume anything else about the inputs, however (hint: there
are still at least a couple of ways for the user to make invalid input,
e.g. trying to write “done” too early).

After adding each piece, there should be either a confirmation that it was
added successfully, or an error message explaining what the issue is.

After the white and the black pieces are added, the program should print
out the black pieces, if any, that the white piece can take.
"""
