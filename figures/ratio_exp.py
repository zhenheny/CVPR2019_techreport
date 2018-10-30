import numpy as np
import matplotlib.pyplot as plt

res = np.array([[0,8.72],[2.5,13.32], [5, 18.26], [12.5,23.87], [18, 26.47], [25,29.37], [50, 33.64], [75, 35.51], [100, 36.67]])
res2 = np.array([[0,0],[2.5,5.64], [5,8.67], [12.5,14.29], [18, 17.67], [25,21.36], [50, 28.74], [75, 32.31], [100, 33.87]])
res3 = np.array([[0,1.22],[2.5,8.21], [5,10.87], [12.5,15.89], [18, 19.87], [25,23.06], [50, 29.34], [75, 32.29], [100, 34.21]])
res = res.T
res2 = res2.T
res3 = res3.T

plt.figure()
plt.cla()
plt.plot(res[0], res[1])
plt.plot(res2[0], res2[1])
plt.plot(res3[0], res3[1])
plt.xlabel('Percentage of available supervision used in training (%)')
plt.ylabel('mAP (%)')
plt.legend(['ours (semi-supervised)', 'ours (fully supervised)', 'R*CNN (semi-supervised)'])
plt.savefig('ratio_exp.pdf')