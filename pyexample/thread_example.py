""" this example shows two threads trying to modify the same variable x, since threads get the CPU in an non-deterministic manner, it is possible that either one finishes first. 
So if one executes this scripts multiple times, one can see sometimes A wins and sometimes B wins. However, sine they are not started at exactly the same time (due to GIL of python), it is more likely that A wins if we write t1.start() above t2.start(), but B still has a chance to win.
"""

import threading

def increase_x(x):
    while x < 10:
        x += 1
    print("A finishes")
    
def decrease_x(x):
    while x > -10:
        x -= 1
    print("B finishes")
    
if __name__ == "__main__":
    x = 0
    t1 = threading.Thread(target=increase_x, args=(x,))
    t2 = threading.Thread(target=decrease_x, args=(x,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()