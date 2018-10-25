import numpy as np
import matplotlib.pyplot as plt

res = np.array([[0,8.72],[100,12.32], [500,20.87], [1000,28.67], [2000, 31.24],[4000, 36.67]])
res2 = np.array([[0,0],[100,8.24], [500,13.29], [1000,24.36], [2000, 28.74],[4000, 36.67]])
res = res.T
res2 = res2.T

plt.figure()
plt.cla()
plt.plot(res[0], res[1])
plt.plot(res2[0], res2[1])
plt.xlabel('number of supervision per class')
plt.ylabel('mAP (%)')
plt.legend(['weakly supervised setup', 'fully supervised setup'])
plt.savefig('ratio_exp.pdf')