# Multiplayer chess
# Allows N players
# Randomly assign two players to start a game
# Store the history and scores of all games played by a player

"""
Other requirements
 - Design a Chess board - Chess Class
 - Scoring - On winning 1, Losing - 0, Draw - 0.5
"""


class Color:
    BLACK = "BLACK"
    WHITE = "WHITE"


class Interface:
    def __init__(self) -> None:
        self.user = self.get_user()

    def get_user(self):
        # Authentication service to provide status on User
        user = None
        return user

    def createGame(self):
        user1 = self.user
        user2 = None
        self.board = Board(user1, user2)


class Board:
    def __init__(self, user1, user2) -> None:
        self.user1 = user1
        self.user2 = user2
        self.initializeGame(user1, user2)
        self.status = "ACTIVE"
        self.pieces = {}

    def initializeGame(self, user1, user2):
        user1.color = Color.BLACK
        self.initializePieces(user1, Color.BLACK)

        user2.color = Color.WHITE
        self.initializePieces(user2, Color.WHITE)

    def initializePieces(self, user, color):
        # initialize all 32 pieces for each user
        piece = Piece(user, piece_type, color, position)
        self.pieces[position] = piece

    def make_move(self, user, current_position, next_position):
        current_piece = self.pieces.get(current_position)
        if not current_piece:
            return

        piece_on_next_post = self.pieces.get(next_position)
        if piece_on_next_post:
            if piece_on_next_post.color == user.color:
                return
            piece_on_next_post.status = "INACTIVE"
            if user.handle == self.user1.handle:
                self.user1.pieces_remaining -= 1
                if self.user1.pieces_remaining == 0:
                    self.abort_game(user)
            else:
                self.user2.pieces_remaining -= 1
                if self.user2.pieces_remaining == 0:
                    self.abort_game(self.user2)

        current_piece.make_move(current_position, next_position)
        self.pieces[next_position] = current_piece

    def abort_game(self, user):
        if user.handle == self.user1.handle:
            user.status = "INACTIVE"
        else:
            self.user2.status = "INACTIVE"
        self.status = 'INACTIVE'


class Piece:
    def __init__(self, user, piece_type, color, position) -> None:
        self.user = user
        self.color = color
        self.piece_type = PieceFactory.piece_types(piece_type)
        self.moves = []
        self.current_position = position
        # self.moves = Move(self.user, self.piece_type)

    def make_move(self, next_move):
        is_valid_move = self.piece_type.check_move(
            self.current_position, next_move)
        if not is_valid_move:
            raise Exception()
        move = Move(self.user)
        move.register_move(self.piece_type, self.current_position, next_move)
        self.current_position = next_move


class PieceKind:
    def __init__(self) -> None:
        self.status = "ACTIVE"

    def check_move(self):
        raise Exception("Function not defined")


class PieceHorse(PieceKind):
    def check_move(self, current_move, next_move):
        # check if move is legal
        pass


class PieceKing(PieceKind):
    def check_move(self, current_move, next_move):
        # check if move is legal
        pass


class PieceQueen(PieceKind):
    def check_move(self, current_move, next_move):
        # check if move is legal
        pass


class PieceFactory:
    HORSE = "HORSE"
    PAWN = "PAWN"
    KING = "KING"
    QUEEN = "QUEEN"

    piece_types = {
        HORSE: PieceHorse
    }

    def __init__(self, piece_type) -> None:
        pass


class Move:
    def __init__(self, user) -> None:
        self.user = user

    def get_moves(self, game_id):
        # get all moves for a user
        pass

    def register_move(self, piece_type, current_pos, next_pos):
        # Connect to db and register move
        pass


class User:
    def __init__(self, handle) -> None:
        self.handle = handle


class BoardUser(User):
    def __init__(self) -> None:
        self.pieces_remaining = 32
        self.color = None
        self.status = "ACTIVE"
