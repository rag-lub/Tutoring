# this function draws the board, taking in an array
def draw_board(board):
	print('   |   |')
	print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' +board[3] + ' | ' + board[4] + ' | ' + board[5])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' +board[0] + ' | ' + board[1] + ' | ' + board[2])
	print('   | ' '  |')
	return None
# this function takes in teString representation, 'X' or 'O' of the current piece
# and switches it to the other.
def change_active_piece(piece):
# if piece equals X, then set piece to O
	if piece == 'X':
		return 'O'
	else:
		return 'X'
# otherwise, if piece equals O, set piece to X
# return piece. Also possible to return within the if statement blocks

# this function takes in the current array of the board and the current piece.
# prmopts for a 'move' (i.e., number 1-9, signifying a space on the board) from
# the user and updates the board array.
# this function redraws the board at the end by calling the draw_board function.
	
def get_move(board, piece):
# some variable to keep track of whether the move is valid
# move = empty string
    move=''
# loop until there's a valid move
    while True:
                
                move = int(input('Enter a valid move (1-9): '))
                if board[move-1] != ' ':
                        print('Invalid move')
                        continue
# if it is, then prompt them to enter a new move
# otherwise, if it's a valid move, then:
                else:
                        board[move-1] = piece
                        #draw_board(board)
                        break
    #return board
# update the signified position (1-9) with the current player's piece
# note: the position in the array is -1, due to 0-based indexing
# note: remember to cast input as a int, because it is a string
# redraw the board with the successful move

# this function takes in a board and the current piece in play
# to check if after a move, there is a winner
# return True if a win, otherwise return False
6
def check_for_win(board, piece):
# winning strings: 'XXX' 'OOO'
	win_combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[6,4,2],[0,4,8]]
	for combo in win_combos:
		winning_string = piece + piece + piece
		if winning_string == board[combo[0]]+board[combo[1]]+board[combo[2]]:
			print(piece + ' wins!')
			return True
	return False

# Check all the possible win combinations and see if they are all the same
# if it's a win, return True
# otherwise, return False
# this function starts the game and facilitates the game
	
def start():
	activeGame = True
# create the board
	board = [' '] * 9
# start with player X
	piece = 'X'
# keep track of if there's a win for looping purposes
	win = False
# while you're in 'activeGame' or there isn't a win or, etc.
	while activeGame:
		draw_board(board)	
		get_move(board,piece)
		win = check_for_win(board,piece)
		if ' ' not in board or win == True:
			activeGame = False
			draw_board(board)	
			print('Game Over.')
		piece = change_active_piece(piece)
# keep switching players, seeing if there's a win after each move,
# prompting for new moves
# when there's a completed game, stop the loop
# signify that the game is over after the loop is done executing
start()
