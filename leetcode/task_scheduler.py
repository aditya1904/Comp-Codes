from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = defaultdict(lambda : 0)
        for task in tasks:
            freq[task] += 1
        sorted_freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
        most_freq = sorted_freq[0][1]
        min_length = (most_freq - 1) * (n + 1)
        additional_len = 0
        for elem in sorted_freq:
            if elem[1] == most_freq:
                additional_len += 1
        return max(len(tasks), min_length + additional_len)