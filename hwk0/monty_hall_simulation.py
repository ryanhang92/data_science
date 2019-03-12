import random
import numpy as np

"""
Function
--------
simulate_prizedoor

Generate a random array of 0s, 1s, and 2s, representing
hiding a prize between door 0, door 1, and door 2

Parameters
----------
nsim : int
    The number of simulations to run

Returns
-------
sims : array
    Random array of 0s, 1s, and 2s

Example
-------
>>> print simulate_prizedoor(3)
array([0, 0, 2])
"""
def simulate_prizedoor(nsim):
    answer = [random.randint(0, 4) for _ in range(nsim)]
    return answer


"""
Function
--------
goat_door

Simulate the opening of a "goat door" that doesn't contain the prize,
and is different from the contestants guess

Parameters
----------
prizedoors : array
    The door that the prize is behind in each simulation
guesses : array
    THe door that the contestant guessed in each simulation

Returns
-------
goats : array
    The goat door that is opened for each simulation. Each item is 0, 1, or 2, and is different
    from both prizedoors and guesses

Examples
--------
>>> print goat_door(np.array([0, 1, 2]), np.array([1, 1, 1]))
>>> array([2, 2, 0])
"""

# Given a the true result of the prize door and matching guess, return
# the door number that is not in that set
# REturn a list of numbers
def goat_door(prizedoor, guesses):
    if len(prizedoor) is not len(guesses):
        raise Exeception('prizedoor and gusses len should be the same')

    goat_doors = []
    door_set = Set(0, 1, 2)
    for i, val in enumerate(range(prizedoor)):
        goat_door =  get_goat_door(door_set, prizedoor, guess)
        goat_doors.append(goat_door)
    return goat_doors

# Returns the number from the set that is not in the list
# It does not matter if prize door == guess door, that
# means the possible goat door guess is more expansive
# TODO: complete the implementation
def get_goat_door(num_set, prize_door, guess_door):
    return 1




"""
Function
--------
switch_guess

The strategy that always switches a guess after the goat door is opened

Parameters
----------
guesses : array
     Array of original guesses, for each simulation
goatdoors : array
     Array of revealed goat doors for each simulation

Returns
-------
The new door after switching. Should be different from both guesses and goatdoors

Examples
--------
>>> print switch_guess(np.array([0, 1, 2]), np.array([1, 2, 1]))
>>> array([2, 0, 0])
"""
#your code here




"""
Function
--------
win_percentage

Calculate the percent of times that a simulation of guesses is correct

Parameters
-----------
guesses : array
    Guesses for each simulation
prizedoors : array
    Location of prize for each simulation

Returns
--------
percentage : number between 0 and 100
    The win percentage

Examples
---------
>>> print win_percentage(np.array([0, 1, 2]), np.array([0, 0, 0]))
33.333
"""
#your code here






'''
Now, put it together. Simulate 10000 games where contestant keeps his original guess, and 10000 games where the contestant switches his door after a goat door is revealed. Compute the percentage of time the contestant wins under either strategy. Is one strategy better than the other?
'''
#your code here


def main():
    print(simulate_prizedoor(5))

# Execute main method
main()
