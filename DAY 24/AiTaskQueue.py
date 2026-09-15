from collections import deque
queue=deque([
    "Load dataset",
    "Clean data",
    "Train model",
    "Validate model",
    "Save model"
])
while queue:
        for i in range(5):
            print(i+1 ,queue[i])
        break

print("processing....")

while queue:
      task=queue.popleft()
      print("completed: ",task)