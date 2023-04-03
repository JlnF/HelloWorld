import time as time
import matplotlib.pyplot as plt
import numpy as np

print(time.time())

a = []
b = []
for i in range(10):
    a.append(i**2)
    b.append(2*i)

plt.plot(a)
plt.plot(b)
plt.savefig("test.png")
