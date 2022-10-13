import sys
input = sys.stdin.readline
INF = int(1e6)

def main():
    def bf(start):
        visit[start] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                for next, cost in roads[j]:
                    if visit[next] > visit[j] + cost:
                        visit[next] = visit[j] + cost
                        if i == n:
                            return True
        return False

    testcase = int(input())
    for _ in range(testcase):
        n, m, w = map(int, input().split())
        roads = [[] for _ in range(n+1)]
        visit = [INF for _ in range(n+1)]
        for _ in range(m):
            s, e, t = map(int, input().split())
            roads[s].append([e, t])
            roads[e].append([s, t])
        for _ in range(w):
            s, e, t = map(int, input().split())
            roads[s].append([e, -t])

        print("YES" if bf(1) else "NO")

if __name__ == '__main__':
    main()