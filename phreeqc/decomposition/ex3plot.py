from pylab import *

res = np.loadtxt('ex3som3.txt', skiprows=2)

plot(res[:, 0], res[:, 1], 'b-', res[:, 0], res[:, 2], 'r-', res[:, 0], res[:, 3], 'm-', res[:, 0], res[:, 4], 'g-')
xlabel('Time (y)')
ylabel('Concentration (mM)')
lgd = plt.legend(('SOM3', 'SOM4', 'CO2', 'NH3'),loc=1,numpoints=1)
lgd.draw_frame(False)
txt = lgd.get_texts()
setp(txt, fontsize='small') 


fig = gcf()
fig.set_size_inches(6, 4)
savefig('ex3.pdf')
#show()
