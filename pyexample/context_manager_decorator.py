from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # Code to run before entering the context
    print("Entering the context")

    try:
        # Code to yield control to the with-block
        yield "Value to be assigned"

    finally:
        # Code to run after exiting the context
        print("Exiting the context")

# Using the context manager
with my_context_manager() as value:
    print("Inside the with-block")
    print("Received value:", value)
    
    
class MyCtxMgr:
    """ Create a custom context manager class 
    """
    def __init__(self):
        # Code to run when the context is created
        print("Entering the context")
    
    def __enter__(self):
        # Code to run when the context is entered
        print("Entering the with-block")
        return "Value to be assigned"
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Code to run when the context is exited
        print("Exiting the with-block")
        print("Exiting the context")
        # Return False to propagate exceptions
        return False

with MyCtxMgr() as m:
    raise ValueError("lalala")