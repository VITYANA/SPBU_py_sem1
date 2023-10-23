from src.Homeworks.homework4.task3.queue import *

if __name__ == "__main__":
    queue = create_queue()
    enqueue(queue, 12)
    enqueue(queue, 15)
    enqueue(queue, 17)
    enqueue(queue, 18)
    print(head(queue), size(queue))
    for i in range(size(queue)):
        print(dequeue(queue), head(queue))
    print(is_empty(queue))
    enqueue(queue, 99)
    print(is_empty(queue), head(queue))
