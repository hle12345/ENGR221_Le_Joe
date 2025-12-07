"""
name: Joe Le
ENGR 221 - Fall 2025
Assignment adapted from HMC CS5
"""

import random  
import time

def rs():
    return random.choice([-1, 1])


def rwpos(start, nsteps):
    
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()
        return rwpos(newpos, nsteps - 1)



def rwsteps(start, low, hi):
    walkway = "_"*(hi-low)
    S = (start-low)
    walkway = walkway[:S] + "S" + walkway[S:]
    walkway = " " + walkway + " "
    print(walkway, "    ", start, low, hi)
    time.sleep(0.05)

    if start <= low or start >= hi:
        return 0
    
    else:
        newstart = start + rs()
        return 1 + rwsteps(newstart, low, hi)


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