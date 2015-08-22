"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """

    max_score = 0
    current_score = 0

    for each_die in hand:
        for each_iteration in hand:
            if each_iteration == each_die:
                current_score += each_iteration
        if current_score > max_score:
            max_score = current_score
        current_score = 0

    return max_score

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = []
    for each_side in range(num_die_sides):
        outcomes.append(each_side + 1)

    rolled_outcomes = gen_all_sequences(tuple(outcomes), num_free_dice)

    running_score = 0.0
    for each_tuple in list(rolled_outcomes):
        hand = held_dice + each_tuple
        running_score += score(hand)

    exp_value = running_score / len(list(rolled_outcomes))

    return exp_value

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """

    all_holds = set([()])
    hand_len = len(hand)

    for each_len in range(hand_len):
        current_holds = gen_all_sequences(hand, each_len + 1)
        for each_tuple in current_holds:
            temp_list = []
            idx = 0
            for each_die in hand:
                if each_die == each_tuple[idx]:
                    temp_list.append(each_die)
                    idx += 1
                    if tuple(temp_list) == each_tuple:
                        all_holds.add(each_tuple)
                        break

    return all_holds

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """

    all_holds = gen_all_holds(hand)
    max_exp_value = 0
    max_tuple = ()

    for each_tuple in all_holds:
        num_free_dice = len(hand) - len(each_tuple)
        current_exp_value = expected_value(each_tuple, num_die_sides, num_free_dice)
        if current_exp_value > max_exp_value:
            max_exp_value = current_exp_value
            max_tuple = each_tuple

    return (max_exp_value, max_tuple)

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    #hand = (1, 1, 1, 5, 6)
    hand = (4, 4)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    print gen_all_holds(hand)
    
#run_example()