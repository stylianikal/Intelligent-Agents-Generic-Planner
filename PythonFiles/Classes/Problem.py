class Problem(object):

    """The abstract class for a formal problem."""

    def __init__(self, initial, goal):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal."""
        if isinstance(self.goal, list):
            return self.goal in state
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
           state1 via action, assuming cost c to get up to state1. If the problem
           is such that the path doesn't matter, this function will only look at
           state2. If the path does matter, it will consider c and maybe state1
           and action. The default method costs 1 for every step in the path."""
        return c + 1
    