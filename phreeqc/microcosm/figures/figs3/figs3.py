from pylab import *

center = loadtxt('../../data/lcp_center.txt')
trough = loadtxt('../../data/lcp_trough.txt')
ridge  = loadtxt('../../data/lcp_ridge.txt')

co8  = np.loadtxt('../../simulations/fe31_co2s/co8.txt', skiprows=2)
cm8  = np.loadtxt('../../simulations/fe31_co2s/cm8.txt', skiprows=2)
ro8  = np.loadtxt('../../simulations/fe31_co2s/ro8.txt', skiprows=2)
rm8  = np.loadtxt('../../simulations/fe31_co2s/rm8.txt', skiprows=2)
to8  = np.loadtxt('../../simulations/fe31_co2s/to8.txt', skiprows=2)
tm8  = np.loadtxt('../../simulations/fe31_co2s/tm8.txt', skiprows=2)

co8a  = np.loadtxt('../../simulations/fe31/co8.txt', skiprows=2)
cm8a  = np.loadtxt('../../simulations/fe31/cm8.txt', skiprows=2)
ro8a  = np.loadtxt('../../simulations/fe31/ro8.txt', skiprows=2)
rm8a  = np.loadtxt('../../simulations/fe31/rm8.txt', skiprows=2)
to8a  = np.loadtxt('../../simulations/fe31/to8.txt', skiprows=2)
tm8a  = np.loadtxt('../../simulations/fe31/tm8.txt', skiprows=2)

totw = [0.013588, 0.005854, 0.011788, 0.006379, 0.010690, 0.006620] #kg   water
totc = [0.045,  0.105, 0.104,  0.105,  0.074, 0.056]                #mol  total organic carbon
scaleco = 100.0/totc[0]
scalecm = 100.0/totc[1]
scalero = 100.0/totc[2]
scalerm = 100.0/totc[3]
scaleto = 100.0/totc[4]
scaletm = 100.0/totc[5]
vwco = totw[0]/1000.0*scaleco # mM to M 
vwcm = totw[1]/1000.0*scalecm
vwro = totw[2]/1000.0*scalero
vwrm = totw[3]/1000.0*scalerm
vwto = totw[4]/1000.0*scaleto
vwtm = totw[5]/1000.0*scaletm

lx = 0.05
ly = 0.85

fig = figure()
ymin = -0.1
ymax = 0.5
index = 15
ax1=subplot(3, 6, 1);
ax1.plot(tm8[:, 0], tm8[:, index]*scaletm, 'r-', tm8a[:, 0], tm8a[:, index]*scaletm, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.yticks([0, 0.2, 0.4])
plt.ylabel('CO$_2$(g)/TOTC (%)')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(a1)', transform=ax1.transAxes)
plt.text(0.4, 1.08, 'trough', transform=ax1.transAxes)

ax2=subplot(3, 6, 2);
ax2.plot(rm8[:, 0], rm8[:, index]*scalerm, 'r-', rm8a[:, 0], rm8a[:, index]*scalerm, 'r--')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(a2)', transform=ax2.transAxes)
plt.text(0.4, 1.08, 'ridge', transform=ax2.transAxes)
plt.text(0.3, 1.30, 'mineral', transform=ax2.transAxes, fontsize=15)

ax3=subplot(3, 6, 3);
ax3.plot(cm8[:, 0], cm8[:, index]*scalecm, 'r-', cm8a[:, 0], cm8a[:, index]*scalecm, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(a3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'center', transform=ax3.transAxes)

ax4=subplot(3, 6, 4);
ax4.plot(to8[:, 0], to8[:, index]*scaleto, 'r-', to8a[:, 0], to8a[:, index]*scaleto, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(a4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'trough', transform=ax4.transAxes)

ax5=subplot(3, 6, 5);
ax5.plot(ro8[:, 0], ro8[:, index]*scalero, 'r-', ro8a[:, 0], ro8a[:, index]*scalero, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(a5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'ridge', transform=ax5.transAxes)
plt.text(0.3, 1.30, 'organic', transform=ax5.transAxes, fontsize=15)

ax6=subplot(3, 6, 6);
ax6.plot(co8[:, 0], co8[:, index]*scaleco, 'r-', co8a[:, 0], co8a[:, index]*scaleco, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(a6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'center', transform=ax6.transAxes)

index1 = 6 
ax1=subplot(3, 6, 7);
ax1.plot(tm8[:, 0], tm8[:, index1]*vwtm, 'r-', tm8a[:, 0], tm8a[:, index1]*vwtm, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.yticks([0, 0.2, 0.4])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(b1)', transform=ax1.transAxes)
plt.ylabel('CO$_2$(a) (%)')

ax2=subplot(3, 6, 8);
ax2.plot(rm8[:, 0], rm8[:, index1]*vwrm, 'r-', rm8a[:, 0], rm8a[:, index1]*vwrm, 'r--')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(b2)', transform=ax2.transAxes)

ax3=subplot(3, 6, 9);
ax3.plot(cm8[:, 0], cm8[:, index1]*vwcm, 'r-', cm8a[:, 0], cm8a[:, index1]*vwcm, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(b3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(3, 6,10);
ax4.plot(to8[:, 0], to8[:, index1]*vwto, 'r-', to8a[:, 0], to8a[:, index1]*vwto, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(b4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(3, 6,11);
ax5.plot(ro8[:, 0], ro8[:, index1]*vwro, 'r-', ro8a[:, 0], ro8a[:, index1]*vwro, 'r--')
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.ylim([ymin, ymax])
plt.ylim([-0.5, 5])
plt.text(lx, ly, '(b5)', transform=ax5.transAxes)

ax6=subplot(3, 6, 12);
ax6.plot(co8[:, 0], co8[:, index1]*vwco, 'r-', co8a[:, 0], co8a[:, index1]*vwco, 'r--')
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(b6)', transform=ax6.transAxes)

index = 17
ax1=subplot(3, 6, 13);
ax1.plot(tm8[:, 0], tm8[:, index]*scaletm, 'r-', tm8a[:, 0], tm8a[:, index]*scaletm, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.ylabel('CO$_2$(s)/TOTC (%)')
plt.text(lx, ly, '(c1)', transform=ax1.transAxes)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])
plt.yticks([0, 0.2, 0.4])

ax2=subplot(3, 6, 14);
ax2.plot(rm8[:, 0], rm8[:, index]*scalerm, 'r-', rm8a[:, 0], rm8a[:, index]*scalerm, 'r--')
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(c2)', transform=ax2.transAxes)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])

ax3=subplot(3, 6, 15);
ax3.plot(cm8[:, 0], cm8[:, index]*scalecm, 'r-', cm8a[:, 0], cm8a[:, index]*scalecm, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(c3)', transform=ax3.transAxes)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])

ax4=subplot(3, 6, 16);
ax4.plot(to8[:, 0], to8[:, index]*scaleto, 'r-', to8a[:, 0], to8a[:, index]*scaleto, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(c4)', transform=ax4.transAxes)
plt.setp(ax4.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])

ax5=subplot(3, 6, 17);
ax5.plot(ro8[:, 0], ro8[:, index]*scalero, 'r-', ro8a[:, 0], ro8a[:, index]*scalero, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(c5)', transform=ax5.transAxes)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])

ax6=subplot(3, 6, 18);
ax6.plot(co8[:, 0], co8[:, index]*scaleco, 'r-', co8a[:, 0], co8a[:, index]*scaleco, 'r--')
plt.xlim([-5, 70])
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(c6)', transform=ax6.transAxes)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')
plt.xticks([0, 20, 40, 60])
lgd = plt.legend(('w. adsorption', 'w.o. adsorption'),loc=1,numpoints=1)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='small') 

subplots_adjust(left=0.06, hspace=0.08, right=0.98, wspace=0.08, top=0.88, bottom=0.1)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 4.8)
savefig('figs3.png')
savefig('figs3.pdf')
#show()
