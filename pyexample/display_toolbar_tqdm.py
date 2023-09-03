import time
from multiprocessing import Pool

from tqdm import tqdm


def _foo(my_number):
   square = my_number * my_number
   time.sleep(0.2)
   return square 

if __name__ == '__main__':
    
    total_iter = 10 
    with Pool(processes=2) as p:
        res_list = []
        with tqdm(total=total_iter) as pbar:
            for i, res in enumerate(p.imap_unordered(_foo, range(0, total_iter))):
                pbar.update()
                res_list.append(res)
    print(res_list)
    
    total_iter = 10 
    with Pool(processes=2) as p:
        res_list = [res for res in tqdm(p.imap_unordered(_foo, range(10)), total=10)]
    print(res_list)
    
    result_list = [] 
    for num in tqdm(range(10)):
        result_list.append(_foo(num))