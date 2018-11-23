import Queue

'''
Implement hot potato with queue data structure via https://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationHotPotato.html
'''

def hotPotato(nameList, num):
    nameQueue = Queue.Queue()

    for name in nameList:
        nameQueue.enqueue(name)
    
    counter = num
    while nameQueue.size() > 1:
        while counter > 0:
            nameQueue.enqueue(nameQueue.dequeue())
            counter = counter - 1
        counter = num #reset counter for each round
        nameQueue.dequeue()
    
    return nameQueue.dequeue()

if __name__ == "__main__":
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))    

    

