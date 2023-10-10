from sys import stdin
import queue
from queue import LifoQueue

def reverseKElements(inputQueue, k) :
    n = inputQueue.qsize()

    # Maintain a stack
    s = LifoQueue()

    # Insert K front elements from queue into stack
    for i in range(k):
        s.put(inputQueue.get())

    # Iterate till size of stack is more than 0
    while s.qsize() > 0:
        inputQueue.put(s.get())

    for i in range(n - k):
        inputQueue.put(inputQueue.get())

    # Return the queue
    return inputQueue
    
