import tictactoe as ttt

board = ttt.initial_state()
action = (0,0)

ttt.player(board)
ttt.actions(board)
ttt.result(board, action)
ttt.winner(board)
ttt.terminal(board)
ttt.utility(board)
ttt.minimax(board)
