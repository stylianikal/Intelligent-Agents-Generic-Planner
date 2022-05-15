import functools
from sys import exit
from time import time
from random import seed, randint


def _exit():
    print("Thank you for using our application.")
    exit()


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def state_generator(number_of_blocks):
    # A function which generates a random state for the blocks world problem
    # number_of_blocks - the number of blocks of the problem
    seed(time())  # initialize random seed using time method for more accurate randoms
    no_of_stacks = randint(1, number_of_blocks)  # generate random number of stacks
    state_list = []
    iterator = no_of_stacks

    while iterator >= 0:
        state_list.append([-1, ])  # Add no_of_stacks "non-empty" lists to state_list
        iterator = iterator - 1

    for iterator in range(number_of_blocks):
        stack_number = randint(0, no_of_stacks - 1)  # Add a random block to a random stack
        state_list[stack_number].append(iterator)
        if -1 in state_list[stack_number]:
            state_list[stack_number].remove(-1)

    generated_state = []
    for stack in state_list:
        if -1 not in stack:  # Tuples that remain "empty" (contain -1) are not added to the generated_state list
            generated_state.append(tuple(stack))

    return tuple(generated_state)  # Returning the list as a tuple


def memoize(fn, slot=None, maxsize=32):
    """Memoize fn: make it remember the computed value for any argument list.
    If slot is specified, store result in that slot of first argument.
    If slot is false, use lru_cache for caching the values."""
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        @functools.lru_cache(maxsize=maxsize)
        def memoized_fn(*args):
            return fn(*args)

    return memoized_fn
