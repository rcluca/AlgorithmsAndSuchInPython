"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 1    # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player

tb = provided.TTTBoard(4)

def mc_trial(board, player):
    while tb.check_win() == None:
        pass

def mc_update_scores(scores, board, player):
    pass

def get_best_move(board, scores):
    pass

def mc_move(board, player, trials):
    pass


print tb.__str__()


# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
