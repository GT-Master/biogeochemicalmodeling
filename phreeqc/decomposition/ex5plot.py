import numpy as np
import matplotlib.pyplot as plt

res = np.loadtxt('ex5som1.txt', skiprows=2)
pf  = np.loadtxt('../../pflotran/decomposition/ex5som1-obs-0.tec', skiprows=2)

nc1 = 0.07146
nc2 = 0.07146
nc3 = 0.08575
nc4 = 0.08575
totc  = res[:, 1] + res[:, 2] + res[:, 3] + res[:, 4] + res[:, 5]
totn  = res[:, 1] * nc1  + res[:, 2] * nc2 + res[:, 3] * nc3 + res[:, 4] * nc4 + res[:, 6]

k1 = 8.267e-7 * 86400.0
k2 = 1.630e-7 * 86400.0
k3 = 1.586e-8 * 86400.0
k4 = 1.157e-9 * 86400.0
f1 = 0.28
f2 = 0.46
f3 = 0.55
f4 = 1.0
t = res[:, 0]
c1 = np.exp(-k1 * t) 
c2 = k1 * (1.0 - f1) * (np.exp(-k2 * t) - np.exp(-k1 * t))/ (k1 - k2)

tpf = pf[:, 0] * 365.0

plt.subplot(2, 1, 1)
plt.plot(res[:, 0], res[:, 1], 'b-', res[:, 0], res[:, 2], 'r-', res[:, 0], res[:, 3], 'g-', res[:, 0], res[:, 4], 'm-', res[:, 0], res[:, 5], 'c-', res[:, 0], totc, 'k-')
plt.ylabel('Concentration (mM)')
lgd = plt.legend(('SOM1', 'SOM2', 'SOM3', 'SOM4', 'CO2', 'TOTC'),loc=7)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 
plt.plot(tpf, pf[:, 3], 'b-', tpf, pf[:, 4], 'r-', tpf, pf[:, 5], 'g-', tpf, pf[:, 6], 'm-', tpf, pf[:, 1]*1000.0, 'c-')

plt.subplot(2, 1, 2)
plt.plot(res[:, 0], res[:, 1]*nc1, 'b-', res[:, 0], res[:, 2]*nc2, 'r-', res[:, 0], res[:, 3]*nc3, 'g-', res[:, 0], res[:, 4]*nc4, 'm-', res[:, 0], res[:, 6], 'm-', res[:, 0], totn, 'k-')
plt.xlabel('Time (y)')
plt.ylabel('Concentration (mM)')
plt.ylim([0, 0.1])
lgd = plt.legend(('SOM1', 'SOM2', 'SOM3', 'SOM4', 'NH3', 'TOTN'),loc=7)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 
plt.plot(tpf, pf[:, 3]*nc1, 'b-', tpf, pf[:, 4]*nc2, 'r-', tpf, pf[:, 5]*nc3, 'g-', tpf, pf[:, 6]*nc4, 'm-', tpf, pf[:, 2]*1000.0, 'c-')

fig = plt.gcf()
fig.set_size_inches(6, 8)
plt.savefig('ex5.pdf')
plt.show()
