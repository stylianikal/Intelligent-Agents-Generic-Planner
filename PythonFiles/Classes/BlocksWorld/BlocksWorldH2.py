from PythonFiles.Classes.BlocksWorld.BlocksWorld import BlocksWorld


class BlocksWorldH2(BlocksWorld):
    def h(self, node):
        # This heuristic counts the number of moves that need to be done
        # in order for every block to reach it correct place
        blocks_not_in_place = 0
        goal_stack = None

        for stack in node.state:
            for other_stack in self.goal:
                if stack[0] in other_stack:
                    goal_stack = other_stack
                    break

            for block in stack:
                block_position = stack.index(block)
                if block in goal_stack:
                    if block_position == goal_stack.index(block):
                        continue
                # All blocks above the current block must be moved
                # so that it'll reach its correct place
                blocks_not_in_place = blocks_not_in_place + len(stack) - block_position
                for iterator in range(block_position, len(stack)):
                    stack_block = stack[iterator]
                    stack_position = stack.index(stack_block)
                    # All blocks below stack_block must be moved
                    # in their correct place, but for every block
                    # stack_block must be moved on the table so we add
                    # each move to the final blocks_not_in_place
                    if stack_position != 0:  # If there are blocks below stack_block in the current state
                        for other_stack in self.goal:
                            if stack_block in other_stack:
                                other_position = other_stack.index(stack_block)
                                if other_position != 0:  # If there are blocks below stack_block in the goal state
                                    for iterator_2 in range(0, stack_position):
                                        other_block = stack[iterator_2]
                                        if other_block in other_stack:
                                            if other_stack.index(other_block) < other_position:
                                                blocks_not_in_place += 1
                                                break
        return blocks_not_in_place
