from heapq import heappush, heappop

def find_min_time(source, destination, n, m, green_times, roads):
    # Create a graph to represent the city map with junctions and roads.
    graph = {i: [] for i in range(1, n+1)}

    # Populate the graph with road information.
    for road in roads:
        i, j, lij = road
        graph[i].append((j, lij))
        graph[j].append((i, lij))

    # Initialize a visited set to keep track of visited junctions.
    visited = set()

    # Initialize a dictionary to store the minimum time taken to reach each junction.
    min_times = {i: float('inf') for i in range(1, n+1)}
    min_times[source] = 0

    # Initialize a priority queue to efficiently find the junction with the minimum time.
    pq = [(0, source)]

    # Main loop to process the priority queue.
    while pq:
        # Pop the junction with the minimum time from the priority queue.
        cur_time, cur_junction = heappop(pq)

        # If the current junction is the destination, return the minimum time.
        if cur_junction == destination:
            return cur_time

        # If the current junction has already been visited, skip it.
        if cur_junction in visited:
            continue

        # Mark the current junction as visited.
        visited.add(cur_junction)

        # Process each neighboring junction of the current junction.
        for neighbor, travel_time in graph[cur_junction]:
            # Calculate the waiting time at the current junction's traffic light.
            wait_time = 0
            if cur_time % green_times[cur_junction - 1] != 0:
                wait_time = green_times[cur_junction - 1] - (cur_time % green_times[cur_junction - 1])

            # Calculate the total time to reach the neighboring junction.
            new_time = cur_time + travel_time + wait_time

            # If the calculated time is less than the current minimum time for the neighboring junction,
            # update the minimum time and add the junction to the priority queue.
            if new_time < min_times[neighbor]:
                min_times[neighbor] = new_time
                heappush(pq, (new_time, neighbor))

    # If the destination junction is not reached, return -1 (or an appropriate value indicating no path found).
    return -1


# Test Case 1: Normal Data
source = 1
destination = 4
n = 4
m = 5
green_times = [4, 3, 2, 5]
roads = [(1, 2, 4), (1, 3, 8), (2, 3, 6), (2, 4, 10), (3, 4, 7)]
# print("Test case 1, expected result = 15, actual result =", find_min_time(source, destination, n, m, green_times, roads))  # Output: 15

# Test Case 2: Boundary Data - Single junction
source = 1
destination = 1
n = 1
m = 0
green_times = [5]
roads = []
# print("Test case 2, expected result = 0, actual result =", find_min_time(source, destination, n, m, green_times, roads))  # Output: 0

# Test Case 3: Boundary Data - No roads
source = 1
destination = 3
n = 3
m = 0
green_times = [3, 4, 5]
roads = []
# print("Test case 3, expected result = -1, actual result =", find_min_time(source, destination, n, m, green_times, roads))  # Output: -1

# Test Case 4: Normal Data - Multiple paths with different waiting times
source = 1
destination = 5
n = 5
m = 6
green_times = [4, 3, 2, 5, 1]
roads = [(1, 2, 4), (1, 3, 8), (2, 3, 6), (2, 4, 10), (3, 4, 7), (3, 5, 3), (5, 4, 5)]
# print("Test case 4, expected result = 11, actual result =", find_min_time(source, destination, n, m, green_times, roads))  # Output: 11

# User input test case
# Read source and destination junctions from user input.
# print("Test case for user input. Provide any test case:")
source, destination = map(int, input().split())

# Read the number of junctions (n) and roads (m) from user input.
n, m = map(int, input().split())

# Read the green_times list from user input.
green_times = list(map(int, input().split()))

# Read the roads information from user input.
roads = []
for _ in range(m):
    road = tuple(map(int, input().split()))
    roads.append(road)

# Call the find_min_time function with the extracted input data.
result = find_min_time(source, destination, n, m, green_times, roads)

# Print the result.
print(result)
