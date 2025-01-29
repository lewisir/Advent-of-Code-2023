"""
--- Advent of Code 2023 ---
--- Day 17: Clumsy Crucible ---
https://adventofcode.com/2023/day/17
"""

from time import perf_counter
from queue import PriorityQueue
import heapq

TEST = True

DAY = "17"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT

START_POSITION = (0, 0)
DIRECTIONS = ((0, 1), (1, 0), (-1, 0), (0, -1))
ROTATIONS = {
    (0, 1): [(-1, 0), (1, 0)],
    (1, 0): [(0, -1), (0, 1)],
    (-1, 0): [(0, -1), (0, 1)],
    (0, -1): [(1, 0), (-1, 0)],
}
STRAIGHT_LINE_LIMIT = 2
INFINITY = float("inf")


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    city_map = build_map(data)
    city_map = (
        (1, 8, 7, 1, 1),
        (1, 1, 1, 1, 1),
        (7, 7, 7, 8, 1),
        (8, 8, 8, 2, 1),
        (9, 9, 9, 3, 1),
    )
    print(restricted_a_star(city_map, (0, 0), (4, 4)))


def restricted_a_star(map, start, goal):
    """Use A* to reach the goal returning the path dictionary. This uses a restricted method to get potential neighbours"""
    next_nodes = []
    heapq.heappush(next_nodes, (0, start))
    path_dict = {start: None}
    cost_so_far = {start: 0}
    while next_nodes:
        current = heapq.heappop(next_nodes)[1]
        if current == goal:
            break
        if path_dict[current] is None:
            neighbours = get_initial_neighbours(map, start)
        else:
            direction = position_diff(current, path_dict[current])
            neighbours = get_limited_neighbours(map, current, direction)
        for next in neighbours:
            new_cost = cost_so_far[current] + sum_costs(map, current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + manhatten_dist(goal, next)
                heapq.heappush(next_nodes, (priority, next))
                path_dict[next] = current
    return path_dict


def a_star(map, start, goal):
    """Use A* to reach the goal returning the path dictionary"""
    next_nodes = []
    heapq.heappush(next_nodes, (0, start))
    path_dict = {start: None}
    cost_so_far = {start: 0}
    while next_nodes:
        current = heapq.heappop(next_nodes)[1]
        if current == goal:
            break
        for next in get_current_neighbours(map, current):
            new_cost = cost_so_far[current] + map[next[0]][next[1]]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + manhatten_dist(goal, next)
                heapq.heappush(next_nodes, (priority, next))
                path_dict[next] = current
    return path_dict


def spf(map, start, goal=None):
    """Run SPF and return a dictionary of the paths form the start to all destinations"""
    next_nodes = []
    heapq.heappush(next_nodes, (0, start))
    path_dict = {start: None}
    cost_so_far = {start: 0}
    while next_nodes:
        current = heapq.heappop(next_nodes)[1]
        if current == goal:
            break
        for next in get_current_neighbours(map, current):
            new_cost = cost_so_far[current] + map[next[0]][next[1]]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heapq.heappush(next_nodes, (new_cost, next))
                path_dict[next] = current
    return path_dict


def bfs(map, start):
    """Return a dictionary of the paths from the start position to all destinations"""
    next_nodes = [start]
    path_dict = {start: None}
    while next_nodes:
        current = next_nodes.pop()
        for next in get_current_neighbours(map, current):
            if next not in path_dict:
                next_nodes.append(next)
                path_dict[next] = current
    return path_dict


def get_current_neighbours(map, position):
    """Return the adjacent points to the position"""
    neighbours = []
    for direction in DIRECTIONS:
        neighbour = update_position(position, direction)
        if (
            neighbour[0] >= 0
            and neighbour[0] < len(map)
            and neighbour[1] >= 0
            and neighbour[1] < len(map[0])
        ):
            neighbours.append(neighbour)
    return neighbours


def get_limited_neighbours(map, position, direction):
    """return the neighbours based on the direction used to arrive at the position"""
    neighbours = []
    for rotation in ROTATIONS[direction]:
        for distance in range(STRAIGHT_LINE_LIMIT):
            neighbour = update_position(
                position, multiply_direction(rotation, distance + 1)
            )
            if (
                neighbour[0] >= 0
                and neighbour[0] < len(map)
                and neighbour[1] >= 0
                and neighbour[1] < len(map[0])
            ):
                neighbours.append(neighbour)
    return neighbours


def get_initial_neighbours(map, position):
    """return a list of the initial neighbours that can be used at the start of the map"""
    neighbours = []
    for direction in DIRECTIONS:
        for distance in range(STRAIGHT_LINE_LIMIT):
            neighbour = update_position(
                position, multiply_direction(direction, distance + 1)
            )
            if (
                neighbour[0] >= 0
                and neighbour[0] < len(map)
                and neighbour[1] >= 0
                and neighbour[1] < len(map[0])
            ):
                neighbours.append(neighbour)
    return neighbours


def sum_costs(map, start, destination):
    """return the sum of the costs to get from start to destination which are in a straight line"""
    start_y, start_x = start
    end_y, end_x = destination
    cost = 0
    sequence = []
    if start_x == end_x and start_y != end_y:
        if end_y >= start_y:
            step = 1
        else:
            step = -1
        for y in range(start_y, end_y, step):
            sequence.append((y + step, start_x))
    elif start_x != end_x and start_y == end_y:
        if end_x >= start_x:
            step = 1
        else:
            step = -1
        for x in range(start_x, end_x, step):
            sequence.append((start_y, x + step))
    else:
        return None
    for position in sequence:
        cost += map[position[0]][position[1]]
    return cost


def multiply_direction(direction, multiplier):
    """return a new tuple with each element multiplied"""
    temp_list = []
    for element in direction:
        temp_list.append(element * multiplier)
    return tuple(temp_list)


def check_move(position, destination, direction, path_history):
    """Return True if we can move in direction from the position on the map"""
    copy_ph = path_history.copy()
    copy_ph.append(position)
    if position in path_history:
        return False
    if position[0] < 0 or position[0] > destination[0]:
        return False
    if position[1] < 0 or position[1] > destination[1]:
        return False
    if (position[0] == 0 or position[0] == destination[0]) and direction[1] == -1:
        return False
    if (position[1] == 0 or position[1] == destination[1]) and direction[0] == -1:
        return False
    if count_previous_moves(copy_ph) >= STRAIGHT_LINE_LIMIT:
        return False
    return True


def count_previous_moves(copy_ph):
    """return the number of times the most recent move in the path_history has occured consecutively"""
    count = 0
    if len(copy_ph) < 3:
        return count
    # copy_ph = path_history.copy()
    last_position1 = copy_ph.pop()
    last_position2 = copy_ph.pop()
    most_recent_diff = position_diff(last_position1, last_position2)
    while copy_ph:
        last_position1 = last_position2
        last_position2 = copy_ph.pop()
        diff = position_diff(last_position1, last_position2)
        if diff == most_recent_diff:
            count += 1
        else:
            return count
    return count


def distance(position1, position2):
    """return the distance between the two positions"""
    delta = position_diff(position1, position2)
    return abs(delta[0]) + abs(delta[1])


def manhatten_dist(position1, position2):
    """return the absolute manhatten distance between the two positions"""
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])


def update_position(position, direction):
    """Return a new tuple adding the direction to the position"""
    return (position[0] + direction[0], position[1] + direction[1])


def position_diff(position1, position2):
    """Return the differnece between position1 and position2"""
    return (position1[0] - position2[0], position1[1] - position2[1])


def build_map(data):
    """Return a tuple of tuples from the input data"""
    temp_list = []
    for line in data:
        temp_line_list = []
        for char in line:
            temp_line_list.append(int(char))
        temp_list.append(tuple(temp_line_list))
    return tuple(temp_list)


def get_input_data(filename):
    """function to read in the input data"""
    file_data = []
    with open(filename) as file:
        for line in file:
            file_data.append(line.rstrip("\n"))
    return file_data


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")
