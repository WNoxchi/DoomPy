from time import sleep
from time import time

t0 = time()
sleep(1)
print(time() - t0)
print()
t0 = time()
sleep(0.5)
print(time() - t0)
print()
t0 = time()
sleep(0.01)
print(time() - t0)
