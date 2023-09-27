from cProfile import Profile
from pstats import SortKey, Stats

def fib_no_mem(n):
    return n if n < 2 else fib_no_mem(n-2)+fib_no_mem(n-1)

with Profile() as pr:
    
    fib_no_mem(35)

    Stats(pr).strip_dirs().sort_stats(SortKey.CALLS).print_stats()


memory = dict()

def fib(n):
    
    if n < 2:
        return n
    
    if n in memory.keys():
        return memory[n]
    else:
        res = fib(n-2)+fib(n-1)
        memory[n] = res
        return res

with Profile() as pr:
    
    fib(35)
    
    Stats(pr).strip_dirs().sort_stats(SortKey.CALLS).print_stats()