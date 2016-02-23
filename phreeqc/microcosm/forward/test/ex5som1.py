import numpy as np
import matplotlib.pyplot as plt

res = np.loadtxt('ex5som1.txt', skiprows=1)

totc  = res[:, 2] + res[:, 3]*6.0 + res[:, 4] + res[:, 5] + res[:, 6] + res[:, 7]

plt.plot(res[:, 0], res[:, 4], 'b-', res[:, 0], res[:, 5], 'r-', res[:, 0], res[:, 6], 'g-', res[:, 0], res[:, 7], 'm-', res[:, 0], res[:, 2], 'c-', res[:, 0], res[:, 3]*6.0, 'y-', res[:, 0], totc, 'k-')
plt.ylabel('Concentration (mM)')
lgd = plt.legend(('SOM1', 'SOM2', 'SOM3', 'SOM4', 'CO2', 'Glucose', 'TOTC'),loc=7)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 
plt.xlabel('Time (y)')

fig = plt.gcf()
fig.set_size_inches(6, 4)
plt.savefig('ex5som1.pdf')
plt.show()
