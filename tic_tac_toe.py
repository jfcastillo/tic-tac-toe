import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    
    if(not self.board.count(None) == 0):
      for i, cell in enumerate(self.board):        
        if(cell == _PLAYER_SYMBOL):       
          if (i == 0 or i  == 1 or i  == 2):      
            #VERTICALES    
            if (self.board[i] == _PLAYER_SYMBOL and self.board[i + 3] == _PLAYER_SYMBOL and self.board[i + 6] == _PLAYER_SYMBOL):
              self.winner = _PLAYER
              break
            #DIAGONALES
            elif(i == 0):
              if (self.board[i] == _PLAYER_SYMBOL and self.board[i + 4] == _PLAYER_SYMBOL and self.board[i + 8] == _PLAYER_SYMBOL):
                self.winner = _PLAYER
                break
            elif(i == 2):
              if (self.board[i] == _PLAYER_SYMBOL and self.board[i + 2] == _PLAYER_SYMBOL and self.board[i + 4] == _PLAYER_SYMBOL):
                self.winner = _PLAYER
                break
          #HORIZONTALES
          if (i == 0 or i  == 3 or i  == 6): 
            if (self.board[i] == _PLAYER_SYMBOL and self.board[i + 1] == _PLAYER_SYMBOL and self.board[i + 2] == _PLAYER_SYMBOL):
                self.winner = _PLAYER
                break
        elif(cell == _MACHINE_SYMBOL):
          if (i == 0 or i  == 1 or i  == 2):      
            #VERTICALES    
            if (self.board[i] == _MACHINE_SYMBOL and self.board[i + 3] == _MACHINE_SYMBOL and self.board[i + 6] == _MACHINE_SYMBOL):
              self.winner = _MACHINE
              break
            #DIAGONALES
            elif(i == 0):
              if (self.board[i] == _MACHINE_SYMBOL and self.board[i + 4] == _MACHINE_SYMBOL and self.board[i + 8] == _MACHINE_SYMBOL):
                self.winner = _MACHINE
                self.is_game_over = True
                break
            elif(i == 2):
              if (self.board[i] == _MACHINE_SYMBOL and self.board[i + 2] == _MACHINE_SYMBOL and self.board[i + 4] == _MACHINE_SYMBOL):
                self.winner = _MACHINE
                break
          #HORIZONTALES
          if (i == 0 or i  == 3 or i  == 6): 
            if (self.board[i] == _MACHINE_SYMBOL and self.board[i + 1] == _MACHINE_SYMBOL and self.board[i + 2] == _MACHINE_SYMBOL):
                self.winner = _MACHINE
                break
    #if self.board.count(None) == 0:
    else:
      self.winner = "empate"

    self.print_result()    

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()
    self.board[chosen_cell] = _PLAYER_SYMBOL
    self.is_over()
    

  def machine_turn(self): # TODO: Finish this function by making the machine choose a random cell (use random module)
    """ for i, cell in enumerate(self.board):
      if cell is None:
        self.board[i] = _MACHINE_SYMBOL
        break """
    
    control = True
    while(control):
      i = random.randint(0, 8)
      if self.board[i] is None:
        self.board[i] = _MACHINE_SYMBOL
        control = False
    self.is_over()
      
    

  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
    if(self.winner == 'empate'):
      print("El juego terminado en empate")
      self.is_game_over = True
    elif (self.winner == _PLAYER or self.winner == _MACHINE):
      print("El juego terminado, el ganador es "+self.winner)
      self.is_game_over = True
    
