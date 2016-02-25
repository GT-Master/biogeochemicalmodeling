import numpy as np
import matplotlib.pyplot as plt

res = np.loadtxt('ex2som4.txt', skiprows=1)
rph = np.loadtxt('ex2som4pH.txt', skiprows=1)
rp2 = np.loadtxt('ex2som4pHclm4me.txt', skiprows=1)

totc  = res[:, 1] + res[:, 2] + res[:, 3]*6.0

sc = 365.0

plt.plot(res[:, 0]/sc, res[:, 1], 'b-', res[:, 0]/sc, res[:, 2], 'r-', res[:, 0]/sc, res[:, 3], 'g-', res[:, 0]/sc, totc, 'k-')
plt.xlabel('Time (y)')
plt.ylabel('Concentration (mM)')
lgd = plt.legend(('SOM4', 'CO2', 'Glucose', 'TOTC'),loc=7)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 
plt.plot(rph[:, 0]/sc, rph[:, 1], 'b-.', rph[:, 0]/sc, rph[:, 2], 'r-.', rph[:, 0]/sc, rph[:, 3], 'g-.', rph[:, 0]/sc, totc, 'k-.')
plt.plot(rp2[:, 0]/sc, rp2[:, 1], 'b--', rp2[:, 0]/sc, rp2[:, 2], 'r--', rp2[:, 0]/sc, rp2[:, 3], 'g--', rp2[:, 0]/sc, totc, 'k--')

fig = plt.gcf()
fig.set_size_inches(6, 4)
plt.savefig('ex2som4.pdf')
plt.show()
