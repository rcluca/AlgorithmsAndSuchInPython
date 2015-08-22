"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._cookies_total = 0.0
        self._cookies = 0.0
        self._time = 0.0
        self._cps = 1.0
        self._history_list = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        my_string = "Total Cookies: %s\
                \nAvailable Cookies: %s\
                \nTime Elapsed: %s\
                \nCPS: %s" % (self._cookies_total, self._cookies, self._time, self._cps)
        return my_string

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history_list

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        return math.ceil((cookies - self._cookies) / self._cps)

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time > 0:
            self._time += time
            self._cookies += self._cps * time
            self._cookies_total += self._cps * time

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._cookies >= cost:
            self._cookies -= cost
            self._cps += additional_cps
            self._history_list.append((self._time, item_name, cost, self._cookies_total))

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """

    #clone = build_info.clone()
    #state = ClickerState()

    #while state.get_time() <= duration:
    #    strat = strategy(state.get_cookies(), state.get_cps(), duration - state.get_time(), clone)
    #    if strat == "None":
    #        break
        

    return ClickerState()


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    My cheap strategy
    """

    items = build_info.build_items()
    min_item = build_info.build_items[0]
    min_price = build_info.get_cost[min_item]

    for eachitem in items:
        current_price = build_info.get_cost(eachitem)
        if min_price >= current_price:
            min_price = current_price
            min_item = eachitem

    return min_item

def strategy_expensive(cookies, cps, time_left, build_info):
    """
    My expensive strategy
    """
    return None

def strategy_best(cookies, cps, time_left, build_info):
    """
    My own strategy
    """
    return None

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    #state = simulate_clicker(provided.BuildInfo(), time, strategy)
    #print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """
    run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)

run()