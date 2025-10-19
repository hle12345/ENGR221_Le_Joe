"""
name: Joe Le
ENGR 221 - Fall 2025
Assignment adapted from HMC CS5
"""

import random  
import time

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)

def rwsteps(start, low, hi):
    """ rwsteps models a random walker which
        * is currently at start 
        * is in a walkway from low (usually 0) to hi (max location) 
          
        rwsteps returns the # of steps taken 
        when the walker reaches an edge
    """
    walkway = "_"*(hi-low)    # create a walkway of underscores
    S = (start-low)           # this is our sleepwalker's location, start-low

    walkway = walkway[:S] + "S" + walkway[S:]  # put our sleepwalker, "S", there

    walkway = " " + walkway + " "              # surround with spaces, for now...

    print(walkway, "    ", start, low, hi)     # print everything to keep track...
    time.sleep(0.05)

    if start <= low or start >= hi:            # base case: no steps if we're at an endpt
        return 0
    
    else:
        newstart = start + rs()                # takes one step, from start to newstart
        return 1 + rwsteps(newstart, low, hi)  # counts one step, recurses for the rest!

def rwstepsLoop(start, low, hi):
    """ Loop-based random walk that prints each state and returns the number of steps taken until the walker reaches an endpoint (<= low or >= hi)"""
    steps = 0
    while True: 
        # inline hallway redering (no extra helper functions)
        width = hi - low +1
        if start <= low:
            pos = 0
        elif start >= hi:
            pos = width -1
        else:
            pos = start - low
        hallway = " " +("_" * pos)+ "S" + ("_" * (width - pos -1))
        #exactly 7 spaces before the numbers to satisfy tests
        print(hallway + "       "+f"{start} {low} {hi}")
        

        #stop when we reach ir cross an endpoint
        if start <= low or start >= hi:
            return steps
        #otherwise, take a random step and continue
        start += rs()
        steps += 1
if __name__ == '__main__':
    print(rs())