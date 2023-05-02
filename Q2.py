from collections import defaultdict


def process_test_case(N, M, L, B, roads):
    graph = defaultdict(list)
    for u, v, w in roads:
        graph[u].append(v)
        graph[v].append(u)

    K = 0
    for i in range(1, L):
        if B[i - 1] != B[i]:
            if B[i] not in graph[B[i - 1]]:
                return -1
            K += 1
    return K


def main():
    T = int(input())
    for _ in range(T):
        N, M, L = map(int, input().split())
        B = list(map(int, input().split()))
        roads = [tuple(map(int, input().split())) for _ in range(M)]
        result = process_test_case(N, M, L, B, roads)
        print(result)


if __name__ == "__main__":
    main()
