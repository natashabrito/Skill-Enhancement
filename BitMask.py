# 5. The "Optimal Resource Allocation" (Bitmask DP)
# ○ Problem: You have N tasks and N workers (where N < 20). Each worker has a specific
# cost for each task. Assign exactly one worker to each task such that the total cost is
# minimized.
# ○ Complexity Requirement: Improve upon the O(N!) brute force to O(2^N . N^2) using
# state compression.

def min_cost(cost):
    n = len(cost)
    size = 1 << n

    dp = [float('inf')] * size
    dp[0] = 0

    for mask in range(size):
        i = bin(mask).count("1")

        for j in range(n):
            if not (mask & (1 << j)):
                new_mask = mask | (1 << j)
                dp[new_mask] = min(
                    dp[new_mask],
                    dp[mask] + cost[i][j]
                )

    return dp[-1]


cost = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

print(min_cost(cost))
