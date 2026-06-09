from go_engine.STONE import Stone
from go_engine.BOARD import Board
count_black = 0
count_white = 0
class Game:
    def __init__(self,size,current_player):
        self.current_player = current_player
        self.board = Board(size)
        self.black_captured = 0
        self.white_captured = 0
        self.ko_board = None
        self.black_count,self.white_count = self.board.blank_count_check_touch()
        self.history = []

    def switch_turn(self):# check đổi chỗ 2 người chơi
        if self.current_player == Stone.BLACK.value:
            self.current_player = Stone.WHITE.value
        elif self.current_player == Stone.WHITE.value:
            self.current_player = Stone.BLACK.value
    
    def play(self,row,column): # logic khi check nếu đặt cờ True thì đổi bên
        before_move = [r[:] for r in self.board.board]
        if self.board.Place_Stone(row, column, self.current_player) == True:
            if self.ko_board is not None and self.board.board == self.ko_board:
                print("Nước đi phạm luật KO")
                self.board.board = before_move
                return False
            if self.current_player == Stone.BLACK.value:
                self.black_captured += self.board.last_eat
            elif self.current_player == Stone.WHITE.value:
                self.white_captured += self.board.last_eat
            
            if self.board.last_eat == 1:
                self.ko_board = before_move
            else:
                self.ko_board = None
            
            self.switch_turn()
            return True

        return False

    def show_captured(self):
        print("Đen ăn được:", self.black_captured)
        print("Trắng ăn được:", self.white_captured)        

    def show_board(self):# giúp thao tác in board qua Game luôn không cần qua Board nữa
        self.board.Show_Board()
      
    def show_current_player(self):
        print(f"Người chơi {self.current_player}")

    def pass_turn(self):
        print(f"Ng chơi {self.current_player} nhường lượt")
        self.switch_turn()
        return True
    
    def total_score(self):
        blacK_total = self.black_captured + self.black_count
        white_total = self.white_captured + self.white_count
        if blacK_total > white_total:
            print("Đen thắng")
        elif white_total > blacK_total:
            print("Trắng thắng")
        else:
            print("Hòa")

        return blacK_total, white_total


    def save_state(self):
        snapshot = {
            "board": [r[:] for r in self.board.board],
            "current_player": self.current_player,
            "black_captured": self.black_captured,
            "white_captured": self.white_captured,
            "count": self.count,
            "ko_board": None if self.ko_board is None else [r[:] for r in self.ko_board]
        }
        self.history.append(snapshot)
