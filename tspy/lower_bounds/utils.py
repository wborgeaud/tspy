def get_cost(tour,tsp):
    ans = 0
    for i in range(len(tour)-1):
        ans += tsp.mat[tour[i],tour[i+1]]
    return ans
