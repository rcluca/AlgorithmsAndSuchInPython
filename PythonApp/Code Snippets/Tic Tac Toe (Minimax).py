"""
Mini-max Tic-Tac-Toe Player
"""

#import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
#import codeskulptor
#codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    #clone board
    clone = board.clone()
    score = []
    move = []
    
    if clone.check_win() != None:
        return SCORES[provided.switch_player(player)], (-1, -1)
    
    #get empty squares
    empty_squares = clone.get_empty_squares()
    
    for each_square in empty_squares:
        #if clone.check_win() != player:
        clone.move(each_square[0], each_square[1], player)
        score_move = mm_move(clone, provided.switch_player(player))
        score.append(score_move[0])
        move.append(each_square)

    if player == provided.PLAYERX:
        idx = score.index(max(score))
    else:
        idx = score.index(min(score))
        
    #return score(idx), move(idx)
    return score[idx], move[idx]

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

game = provided.TTTBoard(3)
game.move(0,1,provided.PLAYERX)
#print game.__str__()
game.move(1,1,provided.PLAYERO)
#print game.__str__()
game.move(0,2,provided.PLAYERX)
#print game.__str__()
game.move(0,0,provided.PLAYERO)
#print game.__str__()
game.move(1,2,provided.PLAYERX)
print game.__str__()
print game._board
print game.get_empty_squares()
print mm_move(provided.TTTBoard(3, False, [[3, 2, 2], [1, 3, 2], [1, 1, 1]]), provided.PLAYERO)

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
