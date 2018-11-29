import time
s=time.perf_counter()
for i in range(30):
    a=1+1
    e=time.perf_counter()
    print(e-s)

