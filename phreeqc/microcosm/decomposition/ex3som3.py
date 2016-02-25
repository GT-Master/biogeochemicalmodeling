import numpy as np
import matplotlib.pyplot as plt

res = np.loadtxt('ex3som3.txt', skiprows=1)

totc  = res[:, 1] + res[:, 2] + res[:, 3] + res[:, 4]*6.0

sc = 365.0

plt.plot(res[:, 0]/sc, res[:, 1], 'b-', res[:, 0]/sc, res[:, 2], 'r-', res[:, 0]/sc, res[:, 3], 'g-', res[:, 0]/sc, res[:, 4], 'm-', res[:, 0]/sc, totc, 'k-')
plt.xlabel('Time (y)')
plt.ylabel('Concentration (mM)')
lgd = plt.legend(('SOM3', 'SOM4', 'CO2', 'Glucose', 'TOTC'),loc=7)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 

fig = plt.gcf()
fig.set_size_inches(6, 4)
plt.savefig('ex3som3.pdf')
plt.show()
