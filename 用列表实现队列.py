from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry 到了
queue.append("Graham")          # Graham 到了
queue.popleft()                 # 第一个到的现在走了

queue.popleft()                 # 第二个到的现在走了

print(queue)                           # 按到达顺序排列的剩余队列