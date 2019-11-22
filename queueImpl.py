from queueClass import Queue


# q = Queue()
# q.enqueue('hello')
# q.enqueue('dog')
# q.enqueue(3)
# print(q)

def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for __ in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
            print(sim_queue)
        sim_queue.dequeue()
    return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent","Brad"], 7))
