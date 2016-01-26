import numpy as np
import matplotlib.pyplot as plt

res = np.loadtxt('ex3som3.txt', skiprows=2)

ncmol = 0.08575  # CN ratio = 10 gC/gN * 12.0111 / 14.0067  
totc  = res[:, 1] + res[:, 2] + res[:, 3]
totn  = res[:, 1] * ncmol  + res[:, 2] * ncmol + res[:, 4]

plt.subplot(2, 1, 1)
plt.plot(res[:, 0], res[:, 1], 'b-', res[:, 0], res[:, 2], 'r-', res[:, 0], res[:, 3], 'g-', res[:, 0], totc, 'k-')
plt.ylabel('Concentration (mM)')
lgd = plt.legend(('SOM3', 'SOM4', 'CO2', 'TOTC'),loc=7)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 

plt.subplot(2, 1, 2)
plt.plot(res[:, 0], res[:, 1]*ncmol, 'b-', res[:, 0], res[:, 2]*ncmol, 'r-', res[:, 0], res[:, 4], 'g-', res[:, 0], totn, 'k-')
plt.xlabel('Time (y)')
plt.ylabel('Concentration (mM)')
plt.ylim([0, 0.1])
lgd = plt.legend(('SOM3', 'SOM4', 'NH3', 'TOTN'),loc=7)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 

fig = plt.gcf()
fig.set_size_inches(6, 8)
plt.savefig('ex3.pdf')
#show()
