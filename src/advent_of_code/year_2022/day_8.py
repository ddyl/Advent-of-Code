"""My solution for year 2022, day 8."""
from advent_of_code import advent_of_code_requests as aoc_requests


def get_input() -> tuple:
    """Gets the challenge input and returns two nested lists, one for rows and\
         one for columns, respectively."""
    input = aoc_requests.get_input("2022", "8").split("\n")
    rows = [[int(i) for i in row] for row in input]
    cols = [[int(row[i]) for row in input] for i in range(0, len(rows[0]))]
    return rows, cols


def part_1_solution() -> int:
    """This function returns the number of visible trees in the challenge input.

    The challenge input provides a map of trees, where each number is the tree height.

    A tree is visible if it is not on the edge of the map, and if it is the tallest
     tree when all the trees above, below, to the left, and to the right of the tree
     are considered.

    Returns:
        int: The number of visible trees.
    """
    # Get rows and columns (cols) as two arrays
    rows, cols = get_input()
    visible_trees = 0

    for row_num, row in enumerate(rows):
        for col_num, height in enumerate(row):
            # Get column of current tree
            col = cols[col_num]

            # If the row is the first row or last row, or
            #  if the column is the first or last column, all trees are visible
            if row_num == 0 or row_num == len(row) - 1:
                visible_trees += 1
            elif col_num == 0 or col_num == len(col) - 1:
                visible_trees += 1
            # If the max height in all directions (up, down, left, right) is equal
            #  to or higher than the current height, pass. Else, tree is visible
            elif (
                max(row[0:col_num]) >= height
                and max(row[col_num + 1 :]) >= height
                and max(col[0:row_num]) >= height
                and max(col[row_num + 1 :]) >= height
            ):
                pass
            else:
                visible_trees += 1

    return visible_trees


def part_2_solution() -> int:
    """Returns the value of the highest scenic score.

    A scenic score for a tree is calculated by taking the number of shorter trees\
         in the above, below, left, and right directions, and multiplying those\
             numbers together.

    In each direction, the number of shorter trees are counted only until a tree\
         of equivalent height or taller is found, or until an edge tree is found.

    Returns:
        int: the highest scenic score of the map.
    """
    # Only rows can be used for this part
    rows = get_input()[0]
    row_count = len(rows[0])
    col_count = len(rows)

    # The directions to search for shorter trees in
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    # Global maximum sccenic score
    max_scenic_score = 0

    for row in range(1, row_count):
        for col in range(1, col_count):

            # Since scenic scores are a multiplication product, initiate to 1, not 0
            local_scenic_score = 1

            for direction in directions:
                shorter_trees = 0
                m_row = row  # m_row is modified row
                m_col = col  # m_col is modified column

                while True:
                    # Counts are done inclusive of taller/equivalent trees.
                    # So, increment by 1 before moving in the direction.
                    shorter_trees += 1
                    m_row += direction[0]
                    m_col += direction[1]

                    # Stop if we reach the edge
                    if m_row <= 0 or m_row >= row_count - 1:
                        break
                    elif m_col <= 0 or m_col >= col_count - 1:
                        break

                    # Stop if we find a tree that is just as tall or taller
                    if rows[m_row][m_col] >= rows[row][col]:
                        break

                local_scenic_score *= shorter_trees

            if local_scenic_score > max_scenic_score:
                max_scenic_score = local_scenic_score

    return max_scenic_score


def main() -> tuple:
    """Returns the solution for part 1 and 2 as a tuple."""
    return part_1_solution(), part_2_solution()
