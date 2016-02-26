import numpy as np
import matplotlib.pyplot as plt

TC = np.arange(-20, 51, 1)
TK = TC + 273.15
iTK = 1/TK*1000.0
T0 = 298.15

ftclmcn = np.exp(308.56*(1/71.02-1/(TK-227.13)))
ftclm4 = 1.5**((TK-298.15)/10.0)
ftcentury = 0.56+0.46*np.arctan(0.097*(TC-15.7))
ftrothc = 47.9/(1+np.exp(106.0/(TC+18.3)))

ftq102 = 2.0**((TK-298.15)/10.0)
ftq103 = 3.0**((TK-298.15)/10.0)
ftq104 = 4.0**((TK-298.15)/10.0)

fta1 = np.exp(-50.0e3/8.314 *(1.0/TK - 1.0/298.15))
fta2 = np.exp(-60.0e3/8.314 *(1.0/TK - 1.0/298.15))
fta3 = np.exp(-70.0e3/8.314 *(1.0/TK - 1.0/298.15))
fta4 = np.exp(-80.0e3/8.314 *(1.0/TK - 1.0/298.15))

ftr1 = (TK - 250.0) * (TK - 250.0) / (T0 - 250.0) / (T0 - 250.0)
ftr2 = (TK - 260.0) * (TK - 260.0) / (T0 - 260.0) / (T0 - 260.0)
ftr3 = (TK - 270.0) * (TK - 270.0) / (T0 - 270.0) / (T0 - 270.0)
ftr4 = (TK - 280.0) * (TK - 280.0) / (T0 - 280.0) / (T0 - 280.0)

xtic = [3.094538, 3.193358, 3.298697, 3.411223, 3.531697, 3.660992, 3.800114, 3.950227]
#xtic = [0.003094538, 0.003193358, 0.003298697, 0.003411223, 0.003531697, 0.003660992, 0.003800114, 0.003950227] * 1000.0
xticlabel = [50, 40, 30, 20, 10, 0, -10, -20] 

fig = plt.figure()
plt.subplots_adjust(hspace=0.0001, wspace=0.0001)

ax1a = fig.add_subplot(221)
ax1b = ax1a.twiny()

ax1a.semilogy(iTK, ftclmcn, 'b-', iTK, ftclm4, 'r-.', iTK, ftcentury, 'g--', iTK[5:71], ftrothc[5:71], 'm:', linewidth=2)
ax1a.set_ylabel('f(T)')
ax1a.set_xlim([4, 3])
ax1a.set_ylim([0.01, 10])
lga = ax1a.legend(('CLM-CN', 'CLM4.x', 'Century', 'ROTH-C'), loc=4)
lga.draw_frame(False)
lgt = lga.get_texts()
plt.setp(lgt, fontsize='small')
plt.text(3.9, 9, '(a)')

ax1b.set_xlim([4, 3])
ax1b.set_xticks(xtic)
ax1b.set_xticklabels(xticlabel)
ax1b.set_xlabel('$^\circ$C')

ax2a = fig.add_subplot(222)
ax2b = ax2a.twiny()

ax2a.semilogy(iTK, ftclm4, 'b-', iTK, ftq102, 'r-.', iTK, ftq103, 'g--', iTK, ftq104, 'm:', linewidth=2)
ax2a.set_xlim([4, 3])
ax2a.set_ylim([0.01, 10])
lg2 = ax2a.legend(('$\mathrm{Q_{10}}$ = 1.5', '$\mathrm{Q_{10}}$ = 2.0', '$\mathrm{Q_{10}}$ = 3.0', '$\mathrm{Q_{10}}$ = 4.0'), loc=4)
lg2.draw_frame(False)
lgt = lg2.get_texts()
plt.setp(lgt, fontsize='small')
plt.text(3.9, 9, '(b)')

ax2b.set_xlim([4, 3])
ax2b.set_xticks(xtic)
ax2b.set_xticklabels(xticlabel)
ax2b.set_xlabel('$^\circ$C')

ax3 = fig.add_subplot(223)
ax3.semilogy(iTK, fta1, 'b-', iTK, fta2, 'r-.', iTK, fta3, 'g--', iTK, fta4, 'm:', linewidth=2)
ax3.set_xlabel('1000/T ($^\circ$K)')
ax3.set_ylabel('f(T)')
ax3.set_xlim([4, 3])
ax3.set_ylim([0.01, 10])
ax3.set_xticks([3.2, 3.4, 3.6, 3.8, 4.0])
ax3.set_yticks([0.01, 0.1, 1])
lg3= ax3.legend(('$\mathrm{E_{a} = 50 kJ/mol}$', '$\mathrm{E_{a} = 60 kJ/mol}$', '$\mathrm{E_{a} = 70 kJ/mol}$', '$\mathrm{E_{a} = 80 kJ/mol}$'), loc=4)
lg3.draw_frame(False)
lgt = lg3.get_texts()
plt.setp(lgt, fontsize='small')
plt.text(3.9, 5, '(c)')

ax4 = fig.add_subplot(224)
ax4.semilogy(iTK, ftr1, 'b-', iTK[7:71], ftr2[7:71], 'r-.', iTK[17:61], ftr3[17:61], 'g--', iTK[27:71], ftr4[27:71], 'm:', linewidth=2)
ax4.set_xlabel('1000/T ($^\circ$K)')
ax4.set_xlim([4, 3])
ax4.set_ylim([0.01, 10])
lg4 = ax4.legend(('$\mathrm{T_{0} = 250^{\circ}K}$', '$\mathrm{T_{0} = 260^{\circ}K}$', '$\mathrm{T_{0} = 270^{\circ}K}$', '$\mathrm{T_{0} = 280^{\circ}K}$'), loc=4)
lg4.draw_frame(False)
lgt = lg4.get_texts()
plt.setp(lgt, fontsize='small')
plt.text(3.9, 5, '(d)')

xticklabels = ax1a.get_xticklabels() + ax2a.get_xticklabels() 
yticklabels = ax2a.get_yticklabels() + ax4.get_yticklabels() 
plt.setp(xticklabels, visible=False)
plt.setp(yticklabels, visible=False)

fig.set_size_inches(8.5, 6)
plt.savefig('fig2.pdf')
plt.savefig('fig2.png')
plt.show()
