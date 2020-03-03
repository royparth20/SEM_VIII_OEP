from TicTacToe import TicTacToe

# ttt=TicTacToe()

# board=[['o', 'x', 'o'],  
#              ['o', 'x', 'x'],  
#              ['o', 'x', 'o']] 
# ttt.set_board(board)
# ttt.set_player('o')
# ttt.set_opponent('x')
# print(ttt.findBestMove())


import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session() 
print(sess.run(hello))