#!/usr/bin/env python3
# rand.py

import asyncio
import random

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def makerandom(idx, threshold) -> int:
    
    print(c[idx+1] + "initiated makerandom(idx={})".format(idx))
    i = random.randint(0, 10)
    while i < threshold:
        print(c[idx+1] + "random value {} too small, retrying".format(i))
        await asyncio.sleep(idx+1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    
    res = await asyncio.gather(*(makerandom(i, 9 - i) for i in range(3)))
    return res 


if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print("\n {}, {}, {}".format(r1, r2, r3))