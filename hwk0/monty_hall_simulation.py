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
# Bug where 3 is not a valid param for the doors
def simulate_prizedoor(nsim):
    answer = [random.randint(0, 2) for _ in range(nsim)]
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
def goat_door(prize_doors, guesses):
    print("goar door", len(prize_doors), len(guesses))
    if len(prize_doors) != len(guesses):
        raise Exeception('prize)doors and gusses len should be the same')

    goat_doors = []
    door_set = [0, 1, 2]
    for i, val in enumerate(prize_doors):
        goat_door =  get_goat_door(door_set, prize_doors[i], guesses[i])
        goat_doors.append(goat_door)
    return goat_doors

# Need to handle edge case where prize and guess door are the same
# I can just randomize if they are not similar
def get_goat_door(num_set, prize_door, guess_door):
    d_set = set(num_set)
    d_set.remove(prize_door)

    # Random pop, it does not matter
    if prize_door == guess_door:
        return d_set.pop()

    # Normal behaviour
    d_set.remove(guess_door)

    if len(d_set) != 1:
        raise Exception('There should only be one goat door')

    return d_set.pop()

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
'''Return an array of switches (doors that are not)
'''
def switch_guess(guesses, goat_doors):
    num_set = [0, 1, 2]
    new_guesses = []
    for i in range(len(guesses)):
        new_guess = switcher_helper(num_set, guesses[i], goat_doors[i])
        new_guesses.append(new_guess)
    return new_guesses


'''Return a switched value for the guess
'''
def switcher_helper(door_set, guess, goat_door):
    d_set = set(door_set)
    d_set.remove(guess)

    if guess == goat_door:
        return d_set.pop()

    d_set.remove(goat_door)

    if len(d_set) != 1:
        raise Exception('There should only be one switched door')

    return d_set.pop()

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
def win_percentage(guesses, prizedoors):
    total = len(guesses)
    wins = 0.0
    for i in range(total):
        if guesses[i] == prizedoors[i]:
            wins += 1
    return wins/total

'''
Now, put it together. Simulate 10000 games where contestant keeps his original guess, and 10000 games where the contestant switches his door after a goat door is revealed. Compute the percentage of time the contestant wins under either strategy. Is one strategy better than the other?
'''
def main():
    num_sim = 1000

    # Control - no goat door
    p_doors = simulate_prizedoor(num_sim)
    init_guesses = simulate_prizedoor(num_sim)
    control_wr = win_percentage(init_guesses, p_doors)

    # View winrate with goat door experiment
    p_doors = simulate_prizedoor(num_sim)
    init_guesses = simulate_prizedoor(num_sim)
    goat_doors = goat_door(p_doors, init_guesses)
    update_guesses = switch_guess(init_guesses, goat_doors)
    exper_wr = win_percentage(update_guesses, p_doors)

    print("control: {0}, experimental: {1} ".format(control_wr, exper_wr))


# Execute main()
main()
