import time
import random
def sem_end(test_data):
    return sum(test_data)

t1=time.perf_counter()
test_data=sem_end(range(10000))
t2=time.perf_counter()
print("Timer for 10 seconds")
for i in range(10):
    print(f"Timer:{i+1} seconds",end="\r")
    time.sleep(1)
print(f"Sum is {test_data} for that time elapsed is {t2-t1:.10f} seconds")
print("Now Time is:",time.clock_gettime(time.CLOCK_REALTIME))



