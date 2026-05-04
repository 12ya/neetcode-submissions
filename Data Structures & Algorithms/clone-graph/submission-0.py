"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque([node])

        clone_map = {}

        clone_map[node] = Node(node.val)

        while queue:
            current_node = queue.popleft()
            
            for neigh in current_node.neighbors:
                if neigh not in clone_map:
                    clone_map[neigh] = Node(neigh.val)
                    queue.append(neigh)
                clone_map[current_node].neighbors.append(clone_map[neigh])
        return clone_map[node]

