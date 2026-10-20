class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        k+=1
        # Making Adjaceny List
        adj = [[] for _ in range(n+1)]
        for s,d,p in flights: adj[s].append((d,p))

        dist = [[INF]*(k+1) for _ in range(n+1)]

        dist[src] = [0]*(k+1)

        HEAP = [(0,src,0)] # Distance, Node, stops
        while HEAP:
            cD,cN,cS = heappop(HEAP)
            if cD>dist[cN][cS]: continue
            for neigh,weight in adj[cN]:
                nD = cD + weight
                if cS+1<=k and nD<dist[neigh][cS+1]:
                    dist[neigh][cS+1] = nD
                    heappush(HEAP,(nD,neigh,cS+1))
        mi = min(dist[dst])
        return -1 if mi == INF else mi