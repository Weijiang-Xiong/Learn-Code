import time

from queue import Queue
from threading import Thread, Event

class Example:
    
    def __init__(self) -> None:
        self.count = 0
        self.buffer = Queue(maxsize=100)
        self._data_ready = Event()
        self._thread = Thread(target=self.background_task, args=())
        self._thread.daemon = True
        self._thread.start()
        time.sleep(5) # by doing this 
    
    def background_task(self):
        
        while True:
            self.buffer.put(self.count+1)
            self.count += 1
            time.sleep(0.5)
            print("Done background task one step")
            self._data_ready.set() 
    
    def foreground_task_step(self, timeout=0.5):
        
        flag = self._data_ready.wait(timeout=timeout)
        # flag = self._data_ready.is_set()
        if not flag:
            raise TimeoutError
        self._data_ready.clear()
        
        return self.buffer.get() 

# now loop to do foreground task 
example = Example()
while True:
    data = example.foreground_task_step()
    print(data)
