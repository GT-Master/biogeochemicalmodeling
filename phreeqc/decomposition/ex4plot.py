import numpy as np
import matplotlib.pyplot as plt

res = np.loadtxt('ex4som2.txt', skiprows=2)

nc2 = 0.07146
nc3 = 0.08575
nc4 = 0.08575
totc  = res[:, 1] + res[:, 2] + res[:, 3] + res[:, 4]
totn  = res[:, 1] * nc2  + res[:, 2] * nc3 + res[:, 3] * nc4 + res[:, 5]

plt.subplot(2, 1, 1)
plt.plot(res[:, 0], res[:, 1], 'b-', res[:, 0], res[:, 2], 'r-', res[:, 0], res[:, 3], 'g-', res[:, 0], res[:, 4], 'm-', res[:, 0], totc, 'k-')
plt.ylabel('Concentration (mM)')
lgd = plt.legend(('SOM2', 'SOM3', 'SOM4', 'CO2', 'TOTC'),loc=7)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 

plt.subplot(2, 1, 2)
plt.plot(res[:, 0], res[:, 1]*nc2, 'b-', res[:, 0], res[:, 2]*nc3, 'r-', res[:, 0], res[:, 3]*nc4, 'g-', res[:, 0], res[:, 5], 'm-', res[:, 0], totn, 'k-')
plt.xlabel('Time (y)')
plt.ylabel('Concentration (mM)')
plt.ylim([0, 0.1])
lgd = plt.legend(('SOM2', 'SOM3', 'SOM4', 'NH3', 'TOTN'),loc=7)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 

fig = plt.gcf()
fig.set_size_inches(6, 8)
plt.savefig('ex4.pdf')
plt.show()
