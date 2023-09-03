import os
import pprint
import multiprocessing as mp
from multiprocessing import Process, Manager, Lock


def single_process_func(d: dict, l: list, idx: int, lock):

    # do the actual work here
    pid = os.getpid()
    d[str(idx)] = "process {} writing to the shared dict using key {}".format(pid, idx)
    l[idx] = "process {} writing to the shared list item {}".format(pid, idx)

    # lock the stdin and out, so the printed lines won't mix up
    lock.acquire()
    print("this is some message from the process {}".format(pid, idx))
    lock.release()


if __name__ == '__main__':

    mp.set_start_method("spawn")
    lock = Lock()

    with Manager() as manager:

        shared_dict = manager.dict()
        shared_list = manager.list(range(5))

        # create a bunch of processes
        workers = []
        for idx in range(5):
            workers.append(Process(target=single_process_func,
                                   args=(shared_dict, shared_list, idx, lock)))

        # start to run the sub processes
        for p in workers:
            p.start()

        # wait for the processes to complete
        for p in workers:
            p.join()

        pprint.pprint(shared_dict._getvalue())
        pprint.pprint(shared_list._getvalue())
