from board.board import Board
from user.user import User

if __name__ == '__main__':
    board = Board(5)
    board.build_board()
    user1 = User()
    user2 = User()

    while True:
        result = board.roll_die(user1)
        print(f"User1 is currently at {(user1.current_x, user1.current_y)}")
        if result:
            print("User1 is the winner")
            break

        result = board.roll_die(user2)
        print(f"User2 is currently at {(user2.current_x, user2.current_y)}")
        if result:
            print("User2 is the winner")
            break
