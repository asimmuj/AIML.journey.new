from collections import deque
queue = deque()
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)
removed = queue.popleft()
print("Removed:", removed)
print(queue)