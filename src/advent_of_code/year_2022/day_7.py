"""My solution for year 2022 day 7."""
from __future__ import annotations

from typing import Optional

from advent_of_code import advent_of_code_requests as aoc_requests


class Node:
    """Defines a directory or file in a file system."""

    def __init__(self, node_name: str, node_type: str, node_size: int) -> None:
        """Initializes a node with the specified node name, type (dir or file)\
             and size."""
        self._node_name = node_name
        self._node_type = node_type
        self._node_size = node_size
        self._node_children: dict[str, Node] = {}

        # If the current Node is root, None is returned
        self._parent: Optional[Node] = None

    def get_node_name(self) -> str:
        """Returns the current node's name."""
        return self._node_name

    def get_node_type(self) -> str:
        """Returns the current node's type (file or dir)."""
        return self._node_type

    def set_node_size(self, size: int) -> None:
        """Sets the current node's size to the supplied value."""
        self._node_size = size

    def get_node_size(self) -> int:
        """Returns the current node's size."""
        return self._node_size

    def get_parent(self) -> Optional[Node]:
        """Returns the parent node."""
        return self._parent

    def add_child(self, node: Node) -> None:
        """Adds node as a child to the current node. Child nodes are stored\
             in dictionaries, where the name of the node is the key, and the node\
                 itself is the value."""
        node._parent = self
        self._node_children[node.get_node_name()] = node

    def get_children(self) -> dict[str, Node]:
        """Returns the child nodes of the current node as a dictionary. The key is the\
             node name, the value is the node itself."""
        return self._node_children


def construct_tree_from_commands(commands: list[str]) -> Node:
    """Constructs the file structure from the given puzzle input.

    Each item in the file directory is a Node class object.

    Args:
        commands (str): The puzzle input.

    Returns:
        Node: The root directory of the constructed file system.
    """
    root_dir = Node(node_name="/", node_size=0, node_type="dir")
    curr_node = root_dir

    for command in commands:
        ins = command.split(" ")  # ins is instructions
        if ins[0] == "$":
            if ins[1] == "cd":
                if ins[2] == "/":
                    curr_node = root_dir
                elif ins[2] == "..":
                    # While technically the parent of the root node is None, this will
                    #  never happen with the given puzzle input
                    parent_node = curr_node.get_parent()
                    curr_node = parent_node if parent_node is not None else curr_node
                else:
                    curr_node = curr_node.get_children()[ins[2]]
            elif ins[1] == "ls":
                pass
        else:
            if ins[0] == "dir":
                new_dir = Node(node_name=ins[1], node_type="dir", node_size=0)
                curr_node.add_child(new_dir)
            else:
                new_file = Node(
                    node_name=ins[1], node_type="file", node_size=int(ins[0])
                )
                curr_node.add_child(new_file)

    return root_dir


def compute_dir_sizes(node: Node, max_size: int = 0, return_list: list = []) -> list:
    """Computes the sizes for all directories using depth-first-search. If `max_size`\
         is given, all directories smaller than `max_size` will be returned.

    Args:
        node (Node): The current/root node.
        max_size (int): The maximum size for a directory. Defaults to 0.
        return_list (list): This holds a list of directories that are smaller than \
            `max_int`. Defaults to [].

    Returns:
        list:  A list containing all directories smaller than the max_size.
    """
    for c in node.get_children().values():
        compute_dir_sizes(c, max_size=max_size, return_list=return_list)

    parent_node = node.get_parent()
    if parent_node is not None:
        size = parent_node.get_node_size()
        parent_node.set_node_size(size + node.get_node_size())
        if node.get_node_type() == "dir" and node.get_node_size() <= max_size:
            return_list.append(node)

    return return_list


def get_input() -> list[str]:
    """Gets the puzzle input from Advent of Code Website."""
    return aoc_requests.get_input("2022", "7").split("\n")


def part_1_solution() -> tuple[int, Node]:
    """Returns the answer for part 1 and the root directory of the constructed file\
         structure as a tuple."""
    commands = get_input()
    root_dir = construct_tree_from_commands(commands)
    nodes_below_max_size = compute_dir_sizes(root_dir, max_size=100000)
    return sum([i.get_node_size() for i in nodes_below_max_size]), root_dir


def part_2_solution(root_dir: Node) -> int:
    """Uses breadth-first-search to find the smallest directory to delete to meet\
     the required memory defined by the input (30000000, with a total memory capacity\
     of 70000000).

    Args:
        root_dir (Node): The root directory of the file structure to evaluate.

    Returns:
        int: The size of the smallest directory to delete.
    """
    unused_memory = 70000000 - root_dir.get_node_size()
    req_memory = 30000000

    dir_to_explore = [root_dir]
    dir_to_delete = []

    while len(dir_to_explore) > 0:
        # Technically, pop() doesn't make this a true breadth-first-search. But this
        #  does give a faster runtime than pop(0), which is O(n).
        curr_dir = dir_to_explore.pop()
        if unused_memory + curr_dir.get_node_size() >= req_memory:
            dir_to_delete.append(curr_dir)
        for v in curr_dir.get_children().values():
            if v.get_node_type() == "dir":
                dir_to_explore.append(v)

    return min([node.get_node_size() for node in dir_to_delete])


def main() -> tuple:
    """Returns the answers for part 1 and part 2 as a tuple."""
    part_1_answer, root_dir = part_1_solution()

    return part_1_answer, part_2_solution(root_dir)
