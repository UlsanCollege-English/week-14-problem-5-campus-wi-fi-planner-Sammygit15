from collections import deque


class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_level_sum(root):
    if root is None:
        return (None, 0)

    queue = deque([root])
    level = 0

    best_level = 0
    best_sum = float('-inf')

    while queue:
        level_size = len(queue)
        current_sum = 0

        # Process one full level
        for _ in range(level_size):
            node = queue.popleft()
            current_sum += node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Check if this level is the new best
        if current_sum > best_sum:
            best_sum = current_sum
            best_level = level

        level += 1

    return (best_level, best_sum)


if __name__ == "__main__":
    # Optional manual tree:
    #       10
    #      /  \
    #     5    7
    #    / \
    #   4   1
    left = TreeNode(5, TreeNode(4), TreeNode(1))
    right = TreeNode(7)
    root = TreeNode(10, left, right)
    print(max_level_sum(root))
