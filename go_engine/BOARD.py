from go_engine.STONE import Stone
class Board:
    def __init__(self,size):
        #Tạo board cho trò chơi
        board = []
        for i in range(size):
            phu = [Stone.EMPTY.value for j in range(size)]
            board.append(phu)
        self.rows = size
        self.columns = size
        self.board = board
        self.last_eat = 0

    def Show_Board(self): #show bàn cờ
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.board[i][j],end=" ")
            print()
           
    
    def Place_Stone(self,row,column,stone):#đặt quân vào bàn cờ
        #check ô có trống không:
        if self.board[row][column] != Stone.EMPTY.value:
            print("Ô đã có quân cờ")
            return False
        else:# nếu ô trống thì đặt quân vào
            backup = [r[:] for r in self.board]# tạo bản sao bàn cờ
            self.board[row][column] = stone
            total_eat = self.eat(row,column)
            self.last_eat = total_eat
            if total_eat > 0:
                print(f"Ăn được {total_eat} quân")
            if self.check_suicide(row,column) == True:
                print("Nước tự sát")
                self.board = backup
                return False
            else:
                return True
        
    
    def find_neighbor(self,row,column): # từ 1 ô tìm các ô xung quanh nó

        neighbors = []
        if 0 <= row - 1 < self.rows and 0 <= column < self.columns:
            neighbors.append((row - 1, column))
        if 0 <= row + 1 < self.rows and 0 <= column < self.columns:
            neighbors.append((row + 1, column))
        if 0 <= row < self.rows and 0 <= column - 1 < self.columns:
            neighbors.append((row, column - 1))
        if 0 <= row < self.rows and 0 <= column + 1 < self.columns:
            neighbors.append((row, column + 1))
        return neighbors

        #up = self.board[row-1][column]
        #down = self.board[row+1][column]
        #left = self.board[row][column-1]
        #right = self.board[row][column+1]

    def get_neighbor_same_color(self,row,column):#tìm các ô cùng màu trong list neighrbor
        neighborsamecol = []
        colormain = self.board[row][column]

        for i,j in self.find_neighbor(row,column):
            if self.board[i][j] == colormain:
                neighborsamecol.append((i,j))

        return neighborsamecol     

    def spread(self,row,column): # tìm tất cả các ô cùng màu trên board
        group = [(row,column)]
        checker = [(row,column)]

        while checker:
            i,j = checker.pop() # lấy phần tử cuối của list đồng thời xóa nó khỏi list

            for x,y in self.get_neighbor_same_color(i,j):
                if (x,y) not in group:
                    group.append((x,y))
                    checker.append((x,y))

        return group

    def liberty(self,row,column):
        for a,b in self.spread(row,column):
            for i,j in self.find_neighbor(a,b):
                if self.board[i][j] == Stone.EMPTY.value:
                    return True
        return False

    def delete_liberty(self,row,column):
        if self.liberty(row,column) == False:
            self.remove_group(row, column)
            return True
        else:
            return False
    
    def remove_group(self, row, column):
        group = self.spread(row, column)
        for a, b in group:
            self.board[a][b] = Stone.EMPTY.value

        return len(group)

    def eat(self,row,column):
        a = self.board[row][column]
        eaten = 0
        for x,y in self.find_neighbor(row,column):
            if self.board[x][y] != a and self.board[x][y] != Stone.EMPTY.value:
                if self.delete_liberty(x,y) == True:
                    print("Bạn ăn quân")
                    eaten = self.remove_group(x,y)
        return eaten
    
    def check_suicide(self,row,column):
        if self.liberty(row,column) == True:
            return False
        else:
            return True
  
    
    def blank_count(self,row,column):
        region = [(row, column)]
        to_check = [(row, column)]

        while to_check:
            i, j = to_check.pop()

            for x, y in self.find_neighbor(i, j):
                if self.board[x][y] == Stone.EMPTY.value and (x, y) not in region:
                    region.append((x, y))
                    to_check.append((x, y))

        return region
    
    def check_touch(self,row,column):
        check = set()
        for x,y in  self.blank_count(row,column):
            for i,j in self.find_neighbor(x,y):
                if self.board[i][j] != Stone.EMPTY.value :
                    check.add(self.board[i][j])
        if check == {Stone.BLACK.value}:
            print("Lãnh thổ đen")
            return "black"
        elif check == {Stone.WHITE.value}:
            print("Lãnh thổ trắng")
            return "white"
        elif check == {Stone.BLACK.value, Stone.WHITE.value}:
            print("Không thuộc ai")
            return None
        

    def blank_count_check_touch(self):
        visited = set()
        black_score = 0
        white_score = 0

        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == Stone.EMPTY.value and (i,j) not in visited:
                    region = self.blank_count(i,j)
                    owner = self.check_touch(i,j)

                    for k in region:
                        visited.add(k)
                    
                    if owner == "black":
                        black_score+=len(region)
                    elif owner == "white":
                        white_score+= len(region)
        return black_score,white_score               
