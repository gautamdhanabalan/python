def print_board(board):
	for index,val in enumerate(board):
		#print(index,val)
		if((index+1)%3 == 0):
			print board[index-1]," ", board[index], " ", board[index+1]	

def win_check(board):
	if(board[1] == 'O' and board[2] == 'O' and board[3] == 'O'):
		print "Player 2 wins"
	
	elif( board[4] == 'O' and board[5] == 'O' and board[6] == 'O'):
		print "Player 2 wins"
	
	elif( board[7] == 'O' and board[8] == 'O' and board[9] == 'O'):
		print "Player 2 wins"
	
	elif(board[1] == 'X' and board[2] == 'X' and board[3] == 'X'):
		print "Player 1 wins"
	
	elif( board[4] == 'X' and board[5] == 'X' and board[6] == 'X'):
		print "Player 1 wins"
	
	elif( board[7] == 'X' and board[8] == 'X' and board[9] == 'X'):
		print "Player 1 wins"
	else:
		print "Game continues"
		return False
	return True	

def full_board_check(board):
	if '-' in board:
		return False
	else:
		return True

def player_choice(marker):
	global board
	print "Input the location number [1-9] on the board to mark"
        position = int(raw_input())	
	if(board[position] == '-'):
		board[position] = marker
		return True 
	else:
		print "location alread filled!! Try again!!"
		return False
'''
Tic Tac Toe main algorithm
'''

board = [0, '-', '-', '-', '-', '-', '-', '-', '-', '-']
print_board(board)

while not full_board_check(board): 
		print "Player 1 choose location"
		while player_choice('X') != True:
			player_choice('X')

		print_board(board)
		if(full_board_check(board)):
			print "Board Full"
			break
		elif(win_check(board)):
			break
		else:
			print "Player 2 choose location"
			while  player_choice('O') != True:
				player_choice('X')
			print_board(board)
			if(full_board_check(board)):
				print "Board Full"
				break
			elif(win_check(board)):
				break
			

