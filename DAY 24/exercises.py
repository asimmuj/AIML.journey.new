# from collections import deque
# queue=deque()
# queue.append("mujtaba")
# queue.append("zeeshan")
# queue.append("ali")
# queue.append("sara")
# print(queue)
# removed=queue.popleft()
# print("removed:",removed)
# print(queue)

# #exercise 2
# from collections import deque
# queue=deque()
# queue.append("download dataset")
# queue.append("clean dataset")
# queue.append("train model")
# queue.append("evaluate model")
# while queue:
#     removed=queue.popleft()
#     print("processing: ",removed)

# #exercise 3
# from collections import deque
# queue=deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.appendleft(10)
# queue.append(50)
# queue.popleft()
# queue.pop()
# print(queue)

#exercise 4
from collections import deque
requests = deque([
    "Request A",
    "Request B",
    "Request C",
    "Request D"
])
while requests:
    task=requests.popleft()
    print("processing:", task)
