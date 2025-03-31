class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def a_star(maze, start, end):

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while open_list:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]


        children = []
        
        adjacent_moves = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for row_move, col_move in adjacent_moves:

            node_position = (current_node.position[0] + row_move, current_node.position[1] + col_move)

            if not valid_move(maze, node_position):
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            
            a_squared = (child.position[0] - end_node.position[0]) ** 2
            b_squared = (child.position[1] - end_node.position[1]) ** 2
            child.h = a_squared + b_squared
            
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)
        
            
def valid_move(maze, node_position):

    if node_position[0] < 0 or node_position[0] >= len(maze):
        return False
    
    if node_position[1] < 0 or node_position[1] >= len(maze[0]):
        return False
    
    if maze[node_position[0]][node_position[1]] != 0:
        return False
    
    return True