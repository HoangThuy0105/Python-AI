from queue import Queue, PriorityQueue


def bfs(graph, start, end):
    frontier = Queue()
    frontier.put(start)
    explored = []

    while True:
        if frontier.empty():
            raise Exception("No way Exception")
        current_node = frontier.get()
        explored.append(current_node)

        # Check if node is goal-node
        if current_node == end:
            return

        for node in graph[current_node]:
            if node not in explored:
                frontier.put(node)


def dfs(graph, start, end):

    frontier = [start, ]
    explored = []

    while True:
        if len(frontier) == 0:
            raise Exception("No way Exception")
        current_node = frontier.pop()
        explored.append(current_node)

        # Check if node is goal-node
        if current_node == end:
            return

        # expanding nodes
        for node in reversed(graph[current_node]):
            if node not in explored:
                frontier.append(node)


def ucs_weight(from_node, to_node, weights=None):
    
    return weights.get((from_node, to_node), 10e100) if weights else 1


def ucs(graph, start, end, weights=None):
    
    frontier = PriorityQueue()
    frontier.put((0, start))  # (priority, node)
    explored = []

    while True:
        if frontier.empty():
            raise Exception("No way Exception")

        ucs_w, current_node = frontier.get()
        explored.append(current_node)

        if current_node == end:
            return

        for node in graph[current_node]:
            if node not in explored:
                frontier.put((
                    ucs_w + ucs_weight(current_node, node, weights),
                    node
                ))


if __name__ == "__main__":
    # This is Tree
    first_graph = {
        'A': ['B', 'C', 'D', 'E'],
        'B': ['A', 'F', 'G'],
        'C': ['A', 'H'],
        'D': ['A', 'I', 'J'],
        'E': ['A', 'K', 'L'],
        'F': ['B', 'M', 'N', 'O'],
        'G': ['B', 'P', 'Q', 'R'],
        'H': ['C', 'S'],
        'I': ['D'],
        'J': ['D', 'T', 'U'],
        'K': ['E'],
        'L': ['E', 'V'],
        'M': ['F'],
        'N': ['F'],
        'O': ['F'],
        'P': ['G'],
        'Q': ['G'],
        'R': ['G'],
        'S': ['H', 'W', 'X'],
        'T': ['J'],
        'U': ['J', 'Y', 'Z'],
        'V': ['L'],
        'W': ['S'],
        'X': ['S'],
        'Y': ['U'],
        'Z': ['U']
    }

    bfs(first_graph, 'A', 'Y')
    dfs(first_graph, 'A', 'Y')
    ucs(first_graph, 'A', 'Y')

    second_graph = {
        'A': ['B', 'C', 'D', 'E'],
        'B': ['A', 'F', 'G', 'H'],
        'C': ['A', 'H'],
        'D': ['A', 'I', 'J'],
        'E': ['A', 'K', 'L'],
        'F': ['B', 'G', 'M', 'N', 'O'],
        'G': ['B', 'F', 'P', 'Q', 'R'],
        'H': ['C', 'G', 'S'],
        'I': ['D'],
        'J': ['D', 'T', 'U'],
        'K': ['E'],
        'L': ['E', 'V'],
        'M': ['F'],
        'N': ['F'],
        'O': ['F'],
        'P': ['G'],
        'Q': ['G'],
        'R': ['G'],
        'S': ['H', 'W', 'X'],
        'T': ['J'],
        'U': ['J', 'Y', 'Z'],
        'V': ['L'],
        'W': ['S'],
        'X': ['S'],
        'Y': ['U'],
        'Z': ['U']
    }
    bfs(second_graph, 'A', 'Y')
    dfs(second_graph, 'A', 'Y')
    ucs(second_graph, 'A', 'Y')