""" This is an example to show how to debug by attaching to a process
in .vscode/launch.json, add a configuration for "remote attach" (the example already added),
use `localhost` for host, and `5678` for port

Then start terminal, check if the folder is opened at the workspace folder then `python pyexample/attach_debug.py`. 
open `pyexample/attach_debug.py` in editor, add breakpoint somewhere, and press f5.
The program should stop at the breakpoint.
If the debugger is disconnected, the process will still run without pausing. 

If you first `cd pyexample` and then `python attach_debug.py`, the breakpoints won't work.
Because vscode is opening a file `pyexample/attach_debug.py` and the python running on `attach_debug.py`, which don't match. 
"""



import debugpy
debugpy.listen(5678)
print("waiting for debugger")
debugpy.wait_for_client()
print("debugger attached")

import time 
def do_something():
    
    while True:
        print(time.time())
        time.sleep(1)
        

if __name__ == "__main__":
    input("hello, please type something")
    do_something()
    
    