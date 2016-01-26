import numpy as np
import matplotlib.pyplot as plt

res = np.loadtxt('ex2som4.txt', skiprows=2)

plt.plot(res[:, 0], res[:, 1], 'b-', res[:, 0], res[:, 2], 'r-', res[:, 0], res[:, 1] + res[:, 2], 'k-')
lgd = plt.legend(('SOM4', 'CO2', 'SOM4+CO2'),loc=7)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 
plt.xlabel('Time (y)')
plt.ylabel('Concentration (mM)')

fig = plt.gcf()
fig.set_size_inches(6, 4)
plt.savefig('ex2.pdf')
#show()
