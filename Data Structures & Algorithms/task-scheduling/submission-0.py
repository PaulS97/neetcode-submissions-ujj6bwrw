class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = {}
        total = len(tasks)
        for task in tasks:
            task_count[task] = task_count.get(task, 0) + 1

        task_heap = list(task_count.values())

        cooldown = deque(n*[0])
        heapq.heapify_max(task_heap)
        rounds = 0
        while(total):
            rounds += 1
            if task_heap:
                count = heapq.heappop_max(task_heap)
                count -= 1
                cooldown.append(count)
                total -= 1
            else:
                cooldown.append(0)

            top = cooldown.popleft()
            if top!=0:
                heapq.heappush_max(task_heap, top)

        return rounds

        