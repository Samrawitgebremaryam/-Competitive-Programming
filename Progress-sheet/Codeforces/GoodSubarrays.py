collections import defaultdict
 
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input()))
    count = defaultdict(int)
    count[0] = 1
 
    summ = ans = 0
    prefix = []
    for i in range(len(nums)):
        summ += nums[i]
        prefix.append(summ)
 
    for r in range(len(prefix)):
        if (prefix[r] - (r + 1)) in count:
            ans += count[prefix[r] - (r + 1)]
        count[prefix[r] - (r + 1)] += 1
    print(ans)