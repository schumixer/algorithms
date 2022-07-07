# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# print(queue.pop(0))
# print(queue)
########################################################################
# from queue import Queue

# q = Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())
# # print(q[0])
########################################################################
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack)
# print(stack.pop())
# print(stack)
########################################################################
from queue import LifoQueue

stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
print(stack.get())
print(stack.get())
print(stack.get())
