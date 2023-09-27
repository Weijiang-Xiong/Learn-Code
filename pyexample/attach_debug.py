""" This is an example to show how to debug by attaching to a process
in .vscode/launch.json, add a configuration for "remote attach",
use `localhost` for host, and `5678` for port

Then start terminal, check if the folder is opened at the workspace folder then `python pyexample/attach_debug.py`. 
open `pyexample/attach_debug.py` in editor, add breakpoint somewhere, and press f5.
The program should stop at the breakpoint.

If you first `cd pyexample` and then `python attach_debug.py`, the breakpoints won't work.
Because vscode is opening a file `pyexample/attach_debug.py` and the python running on `attach_debug.py`, which don't match. 
"""

import numpy as np

import debugpy
debugpy.listen(5678)
print("waiting for debugger")
debugpy.wait_for_client()
print("debugger attached")

def do_something():
    
    while True:
        x = np.random.rand(3,3)
        

if __name__ == "__main__":
    input("hello, please type something")
    do_something()
    
    