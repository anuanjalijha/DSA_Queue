from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue) :
    if inputQueue.empty():
        return
    data = inputQueue.get()
    reverseQueue(inputQueue)
    inputQueue.put(data)    
