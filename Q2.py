from queue import PriorityQueue

def dijkstra(graph, source, destination):
    N = len(graph)
    # Initialize distances from the source to all nodes as infinity
    distances = {v: float('inf') for v in range(1, N+1)}
    distances[source] = 0  # Distance from the source to itself is 0
    pq = PriorityQueue()  # Initialize a priority queue
    pq.put((0, source))  # Add the source node with a distance of 0

    # Process nodes in the priority queue until it is empty
    while not pq.empty():
        (dist, current_vertex) = pq.get()  # Get the node with the minimum distance

        # Update the distances of neighboring nodes if a shorter path is found
        for neighbor, weight in graph[current_vertex]:
            new_cost = dist + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                pq.put((new_cost, neighbor))

    return distances[destination]

def push(distance_list, current_distance):
    # Check the current_distance and update the distance_list and flag accordingly
    # Check if the distance_list is empty
    if len(distance_list) == 0:
        distance_list.append(current_distance)
        flag = 1
    # flag = 1: current_distance is greater than the last element in the distance_list
    elif distance_list[-1] < current_distance:
        distance_list.append(current_distance)
        flag = 1
    # flag = 2: current_distance is equal to the last element in the distance_list
    elif distance_list[-1] == current_distance:
        distance_list.append(current_distance)
        flag = 2
    # flag = 3: current_distance is less than the last element in the distance_list
    else:
        distance_list = []
        flag = 3
    # Return the flag and distance_list
    return flag, distance_list

def find_targeted_city(B, graph):
    targeted = []  # Initialize an empty list to store targeted cities
    left = 0
    right = left + 1
    distance_list = []

    # Iterate through the list of visited cities (B) using the left and right pointers
    while(right < len(B)):
        # Calculate the shortest distance between the cities pointed by left and right pointers
        shortest_distance = dijkstra(graph, B[left], B[right])

        # Update the distance_list and flag based on the shortest distance
        flag, distance_list = push(distance_list, shortest_distance)

        # If flag is 3, add the cities to the targeted list and update the pointers
        if flag == 3:
            if len(targeted) == 0:
                targeted.append(B[left])
            targeted.append(B[right-1])
            left = right - 1
            right = left + 1
        # If flag is 2, add the cities to the targeted list and update the right pointer
        elif flag == 2:
            if len(targeted) == 0:
                targeted.append(B[left])
            targeted.append(B[right-1])
            right += 1
        # If flag is 1, update the right pointer
        elif flag == 1:
            right += 1

    targeted.append(B[-1])

    # If the targeted list has only one city, return -1, otherwise return the number of targeted cities
    if(len(targeted) == 1):
        return -1
    return(len(targeted))

def main():
    T = int(input())  # Read the number of test cases
    result = []  # Initialize an empty list to store the results
    for _ in range(T):
        # Read the input for each test case
        N, M, L = map(int, input().split())
        B = list(map(int, input().split()))
        roads = [tuple(map(int, input().split())) for _ in range(M)]

        # Create the graph using the road information
        graph = {i: [] for i in range(1, N+1)}
        for road in roads:
            i, j, lij = road
            graph[i].append((j, lij))
            graph[j].append((i, lij))

        result.append(find_targeted_city(B, graph))
    for each_result in result:
        print(each_result)

if __name__ == '__main__':
    main()
