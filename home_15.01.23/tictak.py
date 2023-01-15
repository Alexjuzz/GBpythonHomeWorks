class tictakboard : 

    def __init__(self) :
        board  = [[]]
        count  = 0
        point_player1 = 0
        point_player2 = 0
        win_position_ROW = []
        win_position_COL = []
        win_position_DIAG_R = []
        win_position_DIAG_L = []

    def new_game(self):
        self.board  = [['-','-','-']
                      ,['-','-','-']
                      ,['-','-','-']]
        self.count = 0 
        self.point_player1 = 1
        self.point_player2 = -1
                
        self.win_position_ROW = [0,0,0]
        self.win_position_COL = [0,0,0]
        self.win_position_DIAG_R = [0,0,0]
        self.win_position_DIAG_L = [0,0,0]


    def get_field(self):
        print(f'{self.board[0]}\n{self.board[1]}\n{self.board[2]}\n')

    def make_move(self,coordinate_x,coordinate_y):
        win_ROW = self.check_winner(self.win_position_COL)
        win_COL = self.check_winner(self.win_position_ROW)
        if   win_ROW and win_COL:
            self.count = self.count +1
            simbol = ''
            if self.count % 2  == 0 :
                simbol = 'X'
                self.win_position_ROW[coordinate_x-1]  = self.point_player1  + self.win_position_ROW[coordinate_x-1] 
                self.win_position_COL[coordinate_y-1]  = self.point_player1  + self.win_position_COL[coordinate_y-1] 
                if  coordinate_x == coordinate_y :
                        self.win_position_DIAG_L[coordinate_x-1] = self.point_player1  + self.win_position_DIAG_L[coordinate_x-1]
                if coordinate_x + coordinate_y == 4 :
                        self.win_position_DIAG_R[coordinate_x-1] = self.point_player1  + self.win_position_DIAG_R[coordinate_x-1]
        
            else : 
                simbol = '0'
                self.win_position_ROW[coordinate_x-1]  = self.point_player2  + self.win_position_ROW[coordinate_x-1] 
                self.win_position_COL[coordinate_y-1]  = self.point_player2  + self.win_position_COL[coordinate_y-1] 
                if  coordinate_x == coordinate_y :
                        self.win_position_DIAG_L[coordinate_x-1] = self.point_player2  + self.win_position_DIAG_L[coordinate_x-1]
                if coordinate_x + coordinate_y == 4 :
                        self.win_position_DIAG_R[coordinate_x-1] = self.point_player2  + self.win_position_DIAG_R[coordinate_x-1]
                
            if self.board[coordinate_x-1][coordinate_y-1] == '-':
                    self.board[coordinate_x-1][coordinate_y-1] = simbol
                    
            else :
                print(f"{coordinate_x} {coordinate_y}  <- Клетка занята {self.board[coordinate_x-1][coordinate_y-1]}" )
                self.count = self.count-1
            if   self.count == 9:
                print('Draw ! ')
            
    def check_winner(self,s):
        for _ in s :
            if _ == -3 or _ == 3:
                if _ == 3:
                    print("win X")
                    return False
                else: 
                    print('win 0')
                    return False
        return True


a = tictakboard()
a.new_game()

a.make_move(1,1)
a.make_move(2,1)
a.make_move(1,2)

a.make_move(2,2)
a.make_move(1,3)
a.make_move(2,3)

# a.make_move(3,1)
# a.make_move(3,2)
# a.make_move(3,3)
# # print(a.count)
a.get_field()