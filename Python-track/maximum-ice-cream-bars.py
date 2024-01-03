class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total_cost = costs[0]
        count = 0
        while total_cost <= coins and count < len(costs):
            count += 1
            if count < len(costs):
                total_cost += costs[count]
        return count
