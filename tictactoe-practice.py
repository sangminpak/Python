from random import randrange

'''
for i in range(10):
  print(randrange(8))
#this prints 10 random numbers from range 0 to 8, 8 not included
'''
1

  
board=[[3*j+i+1 for i in range(3)] for j in range(3)]
#i have no idea why this works but it works...
board[1][1]="X"

def display_board(board):
  print("+-------"*3,"+",sep="")
  for row in range(3):
    print("|       "*3,"|",sep="")
    for col in range(3):
      print("|   "+str(board[row][col])+"   ",end="")
    print("|")
    print("|       "*3,"|",sep="")
    print("+-------"*3,"+",sep="")



def enter_move(board):
  move=False
  while not move:
    q = int(input("Enter the grid number: "))
    if q == 1:
      if board[0][0] !="O" and board[0][0] !="X":
        board[0][0] = "O"
        display_board(board)
        move = True
      else:
        print("You've entered invalid grid number")
    if q == 2:
      if board[0][1] != "O" and board[0][1] != "X":
        board[0][1] = "O"
        display_board(board)
        move = True
      else:
        print("You've entered invalid grid number.")
    if q == 3:
      if board[0][2] != "O" and board[0][2] != "X":
        board[0][2] = "O"
        display_board(board)
        move = True
      else:
        print("You've entered invalid grid")
    if q == 4:
      if board[1][0] != "O" and board[1][0] != "X":
        board[1][0] = "O"
        display_board(board)
        move = True
      else:
        print("You've entered invalid grid")
    if q == 5:
        print("You've entered invalid grid")
    if q == 6:
      if board[1][2] != "O" and board[1][2] != "X":
        board[1][2] = "O"
        display_board(board)
        move = True
      else:
        print("You've entered invalid grid")
    if q == 7:
      if board[2][0] != "O" and board[2][0] != "X":
        board[2][0] = "O"
        display_board(board)
        move = True
      else:
        print("You've entered invalid grid")
    if q == 8:
      if board[2][1] != "O" and board[2][1] != "X":
        board[2][1] = "O"
        display_board(board)
        move = True
      else:
        print("You've entered invalid grid")
    if q == 9:
      if board[2][2] != "O" and board[2][2] != "X":
        board[2][2] = "O"
        display_board(board)
        move = True
      else:
        print("You've entered invalid grid")
    #move=True
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
  free_list = []
  for row in range(3):
    for col in range(3):
      if board[row][col] != "O" and board[row][col] != "X":
        free_list += [(row,col)]
  print("Free list: ", free_list)
  return free_list



def victory_for(board, sign):
  if sign == "O":
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
      print("You won!")
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
      print("You won!")
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
      print("You won!")
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
      print("You won!")
    else:
      return None
  if sign == "X":
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
      print("Computer won!")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
      print("Computer won!")
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
      print("Computer won!")
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
      print("Computer won!")
    elif board[0][0] == "X" and board[2][2] == "X":
      print("Computer won!")
    elif board[0][2] == "X" and board[2][0] == "X":
      print("Computer won!")
    elif board[1][0] == "X" and board[1][2] == "X":
      print("Computer won!")
    elif board[0][1] =="X" and board[2][1] == "X":
      print("Computer won!")
    else:
      return None
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
  free_list=make_list_of_free_fields(board)
  cnt=len(free_list)
  if cnt > 0:
    this=randrange(cnt)
    row, col =free_list[this]
    board[row][col]="X"
  display_board(board)
  #while game_still_going:
    
  
    # The function draws the computer's move and updates the board.


display_board(board)
free=make_list_of_free_fields(board)

while len(free):
  enter_move(board)
  victory_for(board,"O")
  draw_move(board)
  print("length of free list: ", len(free))
  victory_for(board,"X")
  make_list_of_free_fields(board)
  print("length of free list: ", len(free))
  
print("Tie.")
