from pylab import *

center = loadtxt('../../data/lcp_center.txt')
trough = loadtxt('../../data/lcp_trough.txt')
ridge  = loadtxt('../../data/lcp_ridge.txt')

co2b   = np.loadtxt('../base0/co2.txt', skiprows=1)
co4b   = np.loadtxt('../base0/co4.txt', skiprows=1)
co8b   = np.loadtxt('../base0/co8.txt', skiprows=1)
cm2b   = np.loadtxt('../base0/cm2.txt', skiprows=1)
cm4b   = np.loadtxt('../base0/cm4.txt', skiprows=1)
cm8b   = np.loadtxt('../base0/cm8.txt', skiprows=1)
ro2b   = np.loadtxt('../base0/ro2.txt', skiprows=1)
ro4b   = np.loadtxt('../base0/ro4.txt', skiprows=1)
ro8b   = np.loadtxt('../base0/ro8.txt', skiprows=1)
rm2b   = np.loadtxt('../base0/rm2.txt', skiprows=1)
rm4b   = np.loadtxt('../base0/rm4.txt', skiprows=1)
rm8b   = np.loadtxt('../base0/rm8.txt', skiprows=1)
to2b   = np.loadtxt('../base0/to2.txt', skiprows=1)
to4b   = np.loadtxt('../base0/to4.txt', skiprows=1)
to8b   = np.loadtxt('../base0/to8.txt', skiprows=1)
tm2b   = np.loadtxt('../base0/tm2.txt', skiprows=1)
tm4b   = np.loadtxt('../base0/tm4.txt', skiprows=1)
tm8b   = np.loadtxt('../base0/tm8.txt', skiprows=1)

co2  = np.loadtxt('co2.txt', skiprows=1)
co4  = np.loadtxt('co4.txt', skiprows=1)
co8  = np.loadtxt('co8.txt', skiprows=1)
cm2  = np.loadtxt('cm2.txt', skiprows=1)
cm4  = np.loadtxt('cm4.txt', skiprows=1)
cm8  = np.loadtxt('cm8.txt', skiprows=1)
ro2  = np.loadtxt('ro2.txt', skiprows=1)
ro4  = np.loadtxt('ro4.txt', skiprows=1)
ro8  = np.loadtxt('ro8.txt', skiprows=1)
rm2  = np.loadtxt('rm2.txt', skiprows=1)
rm4  = np.loadtxt('rm4.txt', skiprows=1)
rm8  = np.loadtxt('rm8.txt', skiprows=1)
to2  = np.loadtxt('to2.txt', skiprows=1)
to4  = np.loadtxt('to4.txt', skiprows=1)
to8  = np.loadtxt('to8.txt', skiprows=1)
tm2  = np.loadtxt('tm2.txt', skiprows=1)
tm4  = np.loadtxt('tm4.txt', skiprows=1)
tm8  = np.loadtxt('tm8.txt', skiprows=1)

co2a  = np.loadtxt('../case0g/co2.txt', skiprows=1)
co4a  = np.loadtxt('../case0g/co4.txt', skiprows=1)
co8a  = np.loadtxt('../case0g/co8.txt', skiprows=1)
cm2a  = np.loadtxt('../case0g/cm2.txt', skiprows=1)
cm4a  = np.loadtxt('../case0g/cm4.txt', skiprows=1)
cm8a  = np.loadtxt('../case0g/cm8.txt', skiprows=1)
ro2a  = np.loadtxt('../case0g/ro2.txt', skiprows=1)
ro4a  = np.loadtxt('../case0g/ro4.txt', skiprows=1)
ro8a  = np.loadtxt('../case0g/ro8.txt', skiprows=1)
rm2a  = np.loadtxt('../case0g/rm2.txt', skiprows=1)
rm4a  = np.loadtxt('../case0g/rm4.txt', skiprows=1)
rm8a  = np.loadtxt('../case0g/rm8.txt', skiprows=1)
to2a  = np.loadtxt('../case0g/to2.txt', skiprows=1)
to4a  = np.loadtxt('../case0g/to4.txt', skiprows=1)
to8a  = np.loadtxt('../case0g/to8.txt', skiprows=1)
tm2a  = np.loadtxt('../case0g/tm2.txt', skiprows=1)
tm4a  = np.loadtxt('../case0g/tm4.txt', skiprows=1)
tm8a  = np.loadtxt('../case0g/tm8.txt', skiprows=1)

lx = 0.05
ly = 0.85

fig = figure()
subplots_adjust(left=0.07, hspace=0.08, right=0.95, wspace=0.08)

ax1=subplot(8, 6, 1);
ax1.plot(co2[:, 0], co2[:, 3], 'b-', co4[:, 0], co4[:, 3], 'g-', co8[:, 0], co8[:, 3], 'r-', \
         co2a[:, 0], co2a[:, 3], 'b--', co4a[:, 0], co4a[:, 3], 'g--', co8a[:, 0], co8a[:, 3], 'r--', \
         co2b[:, 0], co2b[:, 3], 'b-.', co4b[:, 0], co4b[:, 3], 'g-.', co8b[:, 0], co8b[:, 3], 'r-.', \
         center[:, 0], center[:, 1], 'b+', center[:, 0], center[:, 2], 'bx', center[:, 0], center[:, 3], 'b.', \
         center[:, 0], center[:, 4], 'g+', center[:, 0], center[:, 5], 'gx', center[:, 0], center[:, 6], 'g.', \
         center[:, 0], center[:, 7], 'r+', center[:, 0], center[:, 8], 'rx', center[:, 0], center[:, 9], 'r.')
plt.xlim([0, 70])
plt.ylim([0, 30])
plt.ylabel('CO$_2$(%)')
plt.yticks([0, 10, 20, 30])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(a1)', transform=ax1.transAxes)
plt.text(0.4, 1.08, 'center', transform=ax1.transAxes)

ax5=subplot(8, 6, 2);
ax5.plot(ro2a[:, 0], ro2a[:, 3], 'b--', ro4a[:, 0], ro4a[:, 3], 'g--', ro8a[:, 0], ro8a[:, 3], 'r--', \
         ro2[:, 0], ro2[:, 3], 'b-', ro4[:, 0], ro4[:, 3], 'g-', ro8[:, 0], ro8[:, 3], 'r-', \
         ro2b[:, 0], ro2b[:, 3], 'b-.', ro4b[:, 0], ro4b[:, 3], 'g-.', ro8b[:, 0], ro8b[:, 3], 'r-.', \
         ridge[:, 0], ridge[:, 1], 'b+', ridge[:, 0], ridge[:, 2], 'bx', \
         ridge[:, 0], ridge[:, 5], 'r+', ridge[:, 0], ridge[:, 6], 'rx', \
         ridge[:, 0], ridge[:, 3], 'g+', ridge[:, 0], ridge[:, 4], 'gx')
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.yticks([0, 10, 20, 30])
plt.xlim([0, 70])
plt.ylim([0, 30])
plt.text(lx, ly, '(a2)', transform=ax5.transAxes)
plt.text(0.4, 1.08, 'ridge', transform=ax5.transAxes)
plt.text(0.3, 1.30, 'organic', transform=ax5.transAxes, fontsize=15)

ax9=subplot(8, 6, 3);
ax9.plot(to2[:, 0], to2[:, 3], 'b-', to4[:, 0], to4[:, 3], 'g-', to8[:, 0], to8[:, 3], 'r-', \
         to2a[:, 0], to2a[:, 3], 'b--', to4a[:, 0], to4a[:, 3], 'g--', to8a[:, 0], to8a[:, 3], 'r--', \
         to2b[:, 0], to2b[:, 3], 'b-.', to4b[:, 0], to4b[:, 3], 'g-.', to8b[:, 0], to8b[:, 3], 'r-.', \
         trough[:, 0], trough[:, 1], 'b+', trough[:, 0], trough[:, 2], 'bx', trough[:, 0], trough[:, 3], 'b.', \
         trough[:, 0], trough[:, 4], 'g+', trough[:, 0], trough[:, 5], 'gx', trough[:, 0], trough[:, 6], 'g.', \
         trough[:, 0], trough[:, 7], 'r+', trough[:, 0], trough[:, 8], 'rx', trough[:, 0], trough[:, 9], 'r.')
plt.yticks([0, 10, 20, 30])
plt.ylim([0, 30])
plt.xlim([0, 70])
plt.text(lx, ly, '(a3)', transform=ax9.transAxes)
plt.setp(ax9.get_xticklabels(), visible=False)
plt.setp(ax9.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'trough', transform=ax9.transAxes)

ax2=subplot(8, 6, 4);
ax2.plot(cm2a[:, 0], cm2a[:, 3], 'b--', cm4a[:, 0], cm4a[:, 3], 'g--', cm8a[:, 0], cm8a[:, 3], 'r--', \
         cm2[:, 0], cm2[:, 3], 'b-', cm4[:, 0], cm4[:, 3], 'g-', cm8[:, 0], cm8[:, 3], 'r-', \
         cm2b[:, 0], cm2b[:, 3], 'b-.', cm4b[:, 0], cm4b[:, 3], 'g-.', cm8b[:, 0], cm8b[:, 3], 'r-.', \
         center[:, 0], center[:, 10], 'b+', center[:, 0], center[:, 11], 'bx', center[:, 0], center[:, 12], 'b.', \
         center[:, 0], center[:, 13], 'g+', center[:, 0], center[:, 14], 'gx', center[:, 0], center[:, 15], 'g.', \
         center[:, 0], center[:, 16], 'r+', center[:, 0], center[:, 17], 'rx', center[:, 0], center[:, 18], 'r.')
plt.xlim([0, 70])
plt.ylim([0, 30])
plt.text(lx, ly, '(a4)', transform=ax2.transAxes)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'center', transform=ax2.transAxes)

ax6=subplot(8, 6, 5);
ax6.plot(rm2[:, 0], rm2[:, 3], 'b-', rm4[:, 0], rm4[:, 3], 'g-', rm8[:, 0], rm8[:, 3], 'r-', \
         rm2a[:, 0], rm2a[:, 3], 'b--', rm4a[:, 0], rm4a[:, 3], 'g--', rm8a[:, 0], rm8a[:, 3], 'r--', \
         rm2b[:, 0], rm2b[:, 3], 'b-.', rm4b[:, 0], rm4b[:, 3], 'g-.', rm8b[:, 0], rm8b[:, 3], 'r-.', \
         ridge[:, 0], ridge[:,  7], 'b+', ridge[:, 0], ridge[:,  8], 'bx', ridge[:, 0], ridge[:,  9], 'b.',\
         ridge[:, 0], ridge[:, 10], 'g+', ridge[:, 0], ridge[:, 11], 'gx', ridge[:, 0], ridge[:, 12], 'g.',\
         ridge[:, 0], ridge[:, 13], 'r+', ridge[:, 0], ridge[:, 14], 'rx', ridge[:, 0], ridge[:, 15], 'r.')
plt.xlim([0, 70])
plt.ylim([0, 30])
plt.text(lx, ly, '(a5)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'ridge', transform=ax6.transAxes)
plt.text(0.3, 1.30, 'mineral', transform=ax6.transAxes, fontsize=15)

axa=subplot(8, 6, 6);
axa.plot(tm2[:, 0], tm2[:, 3], 'b-', tm4[:, 0], tm4[:, 3], 'g-', tm8[:, 0], tm8[:, 3], 'r-', \
         tm2a[:, 0], tm2a[:, 3], 'b--', tm4a[:, 0], tm4a[:, 3], 'g--', tm8a[:, 0], tm8a[:, 3], 'r--', \
         tm2b[:, 0], tm2b[:, 3], 'b-.', tm4b[:, 0], tm4b[:, 3], 'g-.', tm8b[:, 0], tm8b[:, 3], 'r-.', \
         trough[:, 0], trough[:, 10], 'b+', trough[:, 0], trough[:, 11], 'bx', trough[:, 0], trough[:, 12], 'b.', \
         trough[:, 0], trough[:, 13], 'g+', trough[:, 0], trough[:, 14], 'gx', trough[:, 0], trough[:, 15], 'g.', \
         trough[:, 0], trough[:, 16], 'r+', trough[:, 0], trough[:, 17], 'rx', trough[:, 0], trough[:, 18], 'r.')
plt.xlim([0, 70])
plt.ylim([0, 30])
plt.text(lx, ly, '(a6)', transform=axa.transAxes)
plt.setp(axa.get_xticklabels(), visible=False)
plt.setp(axa.get_yticklabels(), visible=False)
plt.text(0.4, 1.08, 'trough', transform=axa.transAxes)

ax3=subplot(8, 6, 7);
ax3.plot(co2[:, 0], co2[:, 4], 'b-', co4[:, 0], co4[:, 4], 'g-', co8[:, 0], co8[:, 4], 'r-', \
         co2a[:, 0], co2a[:, 4], 'b--', co4a[:, 0], co4a[:, 4], 'g--', co8a[:, 0], co8a[:, 4], 'r--', \
         co2b[:, 0], co2b[:, 4], 'b-.', co4b[:, 0], co4b[:, 4], 'g-.', co8b[:, 0], co8b[:, 4], 'r-.', \
         center[:, 0], center[:, 19], 'bx', center[:, 0], center[:, 20], 'b+', center[:, 0], center[:, 21], 'b.', \
         center[:, 0], center[:, 22], 'gx', center[:, 0], center[:, 23], 'g+', center[:, 0], center[:, 24], 'g.', \
         center[:, 0], center[:, 25], 'rx', center[:, 0], center[:, 26], 'r+', center[:, 0], center[:, 27], 'r.')
plt.xlim([0, 70])
plt.ylim([0, 5])
plt.yticks([0, 1, 2, 3 ,4])
plt.setp(ax3.get_xticklabels(), visible=False)
plt.text(lx, ly, '(b1)', transform=ax3.transAxes)
plt.ylabel('CH$_4$(%)')

ax7=subplot(8, 6, 8);
ax7.plot(ro2a[:, 0], ro2a[:, 4], 'b--', ro4a[:, 0], ro4a[:, 4], 'g--', ro8a[:, 0], ro8a[:, 4], 'r--', \
         ro2[:, 0], ro2[:, 4], 'b-', ro4[:, 0], ro4[:, 4], 'g-', ro8[:, 0], ro8[:, 4], 'r-', \
         ro2b[:, 0], ro2b[:, 4], 'b-.', ro4b[:, 0], ro4b[:, 4], 'g-.', ro8b[:, 0], ro8b[:, 4], 'r-.', \
         ridge[:, 0], ridge[:, 20], 'rx', ridge[:, 0], ridge[:, 21], 'r+', \
         ridge[:, 0], ridge[:, 16], 'bx', ridge[:, 0], ridge[:, 17], 'b+', \
         ridge[:, 0], ridge[:, 18], 'gx', ridge[:, 0], ridge[:, 19], 'g+')
plt.setp(ax7.get_xticklabels(), visible=False)
plt.setp(ax7.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, 5])
plt.text(lx, ly, '(b2)', transform=ax7.transAxes)
#plt.ylabel('CH$_4$(%)')

axb=subplot(8, 6, 9);
axb.plot(to2[:, 0], to2[:, 4], 'b-', to4[:, 0], to4[:, 4], 'g-', to8[:, 0], to8[:, 4], 'r-', \
         to2a[:, 0], to2a[:, 4], 'b--', to4a[:, 0], to4a[:, 4], 'g--', to8a[:, 0], to8a[:, 4], 'r--', \
         to2b[:, 0], to2b[:, 4], 'b-.', to4b[:, 0], to4b[:, 4], 'g-.', to8b[:, 0], to8b[:, 4], 'r-.', \
         trough[:, 0], trough[:, 19], 'bx', trough[:, 0], trough[:, 20], 'b+', trough[:, 0], trough[:, 21], 'b.', \
         trough[:, 0], trough[:, 22], 'gx', trough[:, 0], trough[:, 23], 'g+', trough[:, 0], trough[:, 24], 'g.', \
         trough[:, 0], trough[:, 25], 'rx', trough[:, 0], trough[:, 26], 'r+', trough[:, 0], trough[:, 27], 'r.')
plt.xlim([0, 70])
plt.ylim([0, 5])
plt.text(lx, ly, '(b3)', transform=axb.transAxes)
plt.setp(axb.get_xticklabels(), visible=False)
plt.setp(axb.get_yticklabels(), visible=False)
#plt.ylabel('CH$_4$(%)')

ax4=subplot(8, 6,10);
ax4.plot(cm2a[:, 0], cm2a[:, 4], 'b--', cm4a[:, 0], cm4a[:, 4], 'g--', cm8a[:, 0], cm8a[:, 4], 'r--', \
         cm2[:, 0], cm2[:, 4], 'b-', cm4[:, 0], cm4[:, 4], 'g-', cm8[:, 0], cm8[:, 4], 'r-', \
         cm2b[:, 0], cm2b[:, 4], 'b-.', cm4b[:, 0], cm4b[:, 4], 'g-.', cm8b[:, 0], cm8b[:, 4], 'r-.', \
         center[:, 0], center[:, 28], 'gx', center[:, 0], center[:, 29], 'g+', center[:, 0], center[:, 30], 'g.', \
         center[:, 0], center[:, 31], 'bx', center[:, 0], center[:, 32], 'b+', center[:, 0], center[:, 33], 'b.', \
         center[:, 0], center[:, 34], 'rx', center[:, 0], center[:, 35], 'r+', center[:, 0], center[:, 36], 'r.')
plt.xlim([0, 70])
plt.ylim([0, 5])
plt.text(lx, ly, '(b4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)
#lgd = plt.legend(('-2$^\circ$C', '+4$^\circ$C', '+8$^\circ$C'),loc=1,numpoints=1)
#lgd.draw_frame(False)
#txt = lgd.get_texts()
#plt.setp(txt, fontsize='small') 

ax8=subplot(8, 6,11);
ax8.plot(rm2[:, 0], rm2[:, 4], 'b-', rm4[:, 0], rm4[:, 4], 'g-', rm8[:, 0], rm8[:, 4], 'r-', \
         rm2a[:, 0], rm2a[:, 4], 'b--', rm4a[:, 0], rm4a[:, 4], 'g--', rm8a[:, 0], rm8a[:, 4], 'r--', \
         rm2b[:, 0], rm2b[:, 4], 'b-.', rm4b[:, 0], rm4b[:, 4], 'g-.', rm8b[:, 0], rm8b[:, 4], 'r-.', \
         ridge[:, 0], ridge[:, 22], 'bx', ridge[:, 0], ridge[:, 23], 'b+', ridge[:, 0], ridge[:, 24], 'b.',\
         ridge[:, 0], ridge[:, 25], 'gx', ridge[:, 0], ridge[:, 26], 'g+', ridge[:, 0], ridge[:, 27], 'g.',\
         ridge[:, 0], ridge[:, 28], 'rx', ridge[:, 0], ridge[:, 29], 'r+', ridge[:, 0], ridge[:, 30], 'r.')
plt.setp(ax8.get_xticklabels(), visible=False)
plt.setp(ax8.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, 5])
plt.text(lx, ly, '(b5)', transform=ax8.transAxes)

axc=subplot(8, 6, 12);
axc.plot(tm2[:, 0], tm2[:, 4], 'b-', tm4[:, 0], tm4[:, 4], 'g-', tm8[:, 0], tm8[:, 4], 'r-', \
         tm2a[:, 0], tm2a[:, 4], 'b--', tm4a[:, 0], tm4a[:, 4], 'g--', tm8a[:, 0], tm8a[:, 4], 'r--', \
         tm2b[:, 0], tm2b[:, 4], 'b-.', tm4b[:, 0], tm4b[:, 4], 'g-.', tm8b[:, 0], tm8b[:, 4], 'r-.', \
         trough[:, 0], trough[:, 28], 'bx', trough[:, 0], trough[:, 29], 'b+', trough[:, 0], trough[:, 30], 'b.', \
         trough[:, 0], trough[:, 31], 'gx', trough[:, 0], trough[:, 32], 'g+', trough[:, 0], trough[:, 33], 'g.', \
         trough[:, 0], trough[:, 34], 'rx', trough[:, 0], trough[:, 35], 'r+', trough[:, 0], trough[:, 36], 'r.')
plt.setp(axc.get_xticklabels(), visible=False)
plt.setp(axc.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, 5])
plt.text(lx, ly, '(b6)', transform=axc.transAxes)

ot1 = [0, 15, 30, 60];
ph2co = [5.02, 5.02, 5.38, 5.71]
ph4co = [5.02, 5.09, 5.62, 5.32]
ph8co = [5.02, 5.09, 5.31, 5.42]

index = 1
offset = 12 
ax1=subplot(8, 6, 13);
ax1.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot1, ph2co, 'b+', ot1, ph4co, 'g+', ot1, ph8co, 'r+')
plt.xlim([0, 70])
plt.ylim([4, 7])
plt.yticks([4, 5, 6])
plt.ylabel('pH')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(c1)', transform=ax1.transAxes)

ax5=subplot(8, 6, 14);
ph2ro = [5.21, 5.50, 6.00, 6.00]
ph4ro = [5.21, 5.21, 5.92, 6.02]
ph8ro = [5.21, 5.21, 5.98, 6.21]
ax5.plot(ro2a[:, 0], ro2a[:, index], 'b--', ro4a[:, 0], ro4a[:, index], 'g--', ro8a[:, 0], ro8a[:, index], 'r--', \
         ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.', \
         ot1, ph2ro, 'b+', ot1, ph4ro, 'g+', ot1, ph8ro, 'r+')
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
#plt.ylabel('pH')
plt.xlim([0, 70])
plt.ylim([4, 7])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(c2)', transform=ax5.transAxes)

ax9=subplot(8, 6, 15);
ph2to = [5.23, 5.20, 5.10, 5.20]
ph4to = [5.23, 5.23, 5.11, 5.76]
ph8to = [5.23, 5.23, 5.55, 6.15]
ax9.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b--', to4a[:, 0], to4a[:, index], 'g--', to8a[:, 0], to8a[:, index], 'r--', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.', \
         ot1, ph2to, 'b+', ot1, ph4to, 'g+', ot1, ph8to, 'r+')
plt.setp(ax9.get_xticklabels(), visible=False)
plt.setp(ax9.get_yticklabels(), visible=False)
#plt.ylabel('pH')
plt.xlim([0, 70])
plt.ylim([4, 7])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(c3)', transform=ax9.transAxes)

ax2=subplot(8, 6, 16);
ph2cm = [4.84, 4.83, 5.67, 4.90]
ph4cm = [4.84, 4.83, 5.74, 5.81]
ph8cm = [4.84, 4.83, 5.89, 6.10]

ax2.plot(cm2a[:, 0], cm2a[:, index], 'b--', cm4a[:, 0], cm4a[:, index], 'g--', cm8a[:, 0], cm8a[:, index], 'r--', \
         cm2[:, 0], cm2[:, index], 'b-', cm4[:, 0], cm4[:, index], 'g-', cm8[:, 0], cm8[:, index], 'r-', \
         cm2b[:, 0], cm2b[:, index], 'b-.', cm4b[:, 0], cm4b[:, index], 'g-.', cm8b[:, 0], cm8b[:, index], 'r-.', \
         ot1, ph2cm, 'b+', ot1, ph4cm, 'g+', ot1, ph8cm, 'r+')
plt.xlim([0, 70])
plt.ylim([4, 7])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(c4)', transform=ax2.transAxes)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)

ax6=subplot(8, 6, 17);
ph2rm = [4.54, 4.50, 5.50, 5.03]
ph4rm = [4.54, 4.54, 5.34, 5.12]
ph8rm = [4.54, 4.54, 4.60, 4.90]
ax6.plot(rm2[:, 0], rm2[:, index], 'b-', rm4[:, 0], rm4[:, index], 'g-', rm8[:, 0], rm8[:, index], 'r-', \
         rm2a[:, 0], rm2a[:, index], 'b--', rm4a[:, 0], rm4a[:, index], 'g--', rm8a[:, 0], rm8a[:, index], 'r--', \
         rm2b[:, 0], rm2b[:, index], 'b-.', rm4b[:, 0], rm4b[:, index], 'g-.', rm8b[:, 0], rm8b[:, index], 'r-.', \
         ot1, ph2rm, 'b+', ot1, ph4rm, 'g+', ot1, ph8rm, 'r+')
plt.xlim([0, 70])
plt.ylim([4, 7])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(c5)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

axa=subplot(8, 6, 18);
ph2tm = [4.95, 5.10, 5.61, 5.90]
ph4tm = [4.95, 4.95, 5.39, 5.61]
ph8tm = [4.95, 4.95, 5.53, 5.98]
axa.plot(tm2[:, 0], tm2[:, index], 'b-', tm4[:, 0], tm4[:, index], 'g-', tm8[:, 0], tm8[:, index], 'r-', \
         tm2a[:, 0], tm2a[:, index], 'b--', tm4a[:, 0], tm4a[:, index], 'g--', tm8a[:, 0], tm8a[:, index], 'r--', \
         tm2b[:, 0], tm2b[:, index], 'b-.', tm4b[:, 0], tm4b[:, index], 'g-.', tm8b[:, 0], tm8b[:, index], 'r-.', \
         ot1, ph2tm, 'b+', ot1, ph4tm, 'g+', ot1, ph8tm, 'r+')
plt.xlim([0, 70])
plt.ylim([4, 7])
plt.yticks([4, 5, 6, 7])
plt.text(lx, ly, '(c6)', transform=axa.transAxes)
plt.setp(axa.get_xticklabels(), visible=False)
plt.setp(axa.get_yticklabels(), visible=False)

index=9
ot3 = [0, 30, 60];
ac2co = [6.37, 14.71, 13.08]
ac4co = [6.37, 17.93,  6.67]
ac8co = [6.37, 21.19,  5.35]
ax1=subplot(8, 6, 19);
ax1.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot3, ac2co, 'b+', ot3, ac4co, 'g+', ot3, ac8co, 'r+')
plt.xlim([0, 70])
plt.ylim([0, 25])
plt.yticks([0, 10,  20])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(d1)', transform=ax1.transAxes)
plt.ylabel('Ac (mM)')
#plt.setp(ax3.get_yticklabels(), fontsize='small')

ax2=subplot(8, 6, 20);
ot2 = [0, 30];
ac2ro = [0.057, 0.24]
ac4ro = [0.057, 0.05]
ac8ro = [0.057, 2.24]
ax2.plot(ro2a[:, 0], ro2a[:, index], 'b--', ro4a[:, 0], ro4a[:, index], 'g--', ro8a[:, 0], ro8a[:, index], 'r--', \
         ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.', \
         ot2, ac2ro, 'b+', ot2, ac4ro, 'g+', ot2, ac8ro, 'r+')
plt.xlim([0, 70])
plt.ylim([0, 25])
plt.text(lx, ly, '(d2)', transform=ax2.transAxes)
#plt.ylabel('Acetate (mM)')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)

ax3=subplot(8, 6,21);
ac2to = [1.03,  3.83,  2.79]
ac4to = [1.03, 93.58,  1.60]
ac8to = [1.03,120.80,  2.30]
ax3.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b--', to4a[:, 0], to4a[:, index], 'g--', to8a[:, 0], to8a[:, index], 'r--', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.', \
         ot3, ac2to, 'b+', ot3, ac4to, 'g+', ot3, ac8to, 'r+')
plt.xlim([0, 70])
plt.ylim([0, 25])
plt.text(lx, ly, '(d3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)
#plt.ylabel('Acetate (mM)')

ax4=subplot(8, 6, 22);
ac2cm = [2.80,  8.50,  0.28]
ac4cm = [2.80,  7.66,  0.32]
ac8cm = [2.80,  6.42,  0.33]
ax4.plot(cm2a[:, 0], cm2a[:, index], 'b--', cm4a[:, 0], cm4a[:, index], 'g--', cm8a[:, 0], cm8a[:, index], 'r--', \
         cm2[:, 0], cm2[:, index], 'b-', cm4[:, 0], cm4[:, index], 'g-', cm8[:, 0], cm8[:, index], 'r-', \
         cm2b[:, 0], cm2b[:, index], 'b-.', cm4b[:, 0], cm4b[:, index], 'g-.', cm8b[:, 0], cm8b[:, index], 'r-.', \
         ot3, ac2cm, 'b+', ot3, ac4cm, 'g+', ot3, ac8cm, 'r+')
plt.xlim([0, 70])
plt.ylim([0, 25])
plt.text(lx, ly, '(d4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(8, 6, 23);
ac2rm = [2.67,  4.70,  0.29]
ac4rm = [2.67,  2.07,  0.29]
ac8rm = [2.67,  2.45,  0.29]
ax5.plot(rm2[:, 0], rm2[:, index], 'b-', rm4[:, 0], rm4[:, index], 'g-', rm8[:, 0], rm8[:, index], 'r-', \
         rm2a[:, 0], rm2a[:, index], 'b--', rm4a[:, 0], rm4a[:, index], 'g--', rm8a[:, 0], rm8a[:, index], 'r--', \
         rm2b[:, 0], rm2b[:, index], 'b-.', rm4b[:, 0], rm4b[:, index], 'g-.', rm8b[:, 0], rm8b[:, index], 'r-.', \
         ot3, ac2rm, 'b+', ot3, ac4rm, 'g+', ot3, ac8rm, 'r+')
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, 25])
plt.text(lx, ly, '(d5)', transform=ax8.transAxes)

ax6=subplot(8, 6, 24);
ac2tm = [1.84,  3.08,  0.27]
ac4tm = [1.84,  2.30,  0.22]
ac8tm = [1.84,  3.81,  0.27]
ax6.plot(tm2[:, 0], tm2[:, index], 'b-', tm4[:, 0], tm4[:, index], 'g-', tm8[:, 0], tm8[:, index], 'r-', \
         tm2a[:, 0], tm2a[:, index], 'b--', tm4a[:, 0], tm4a[:, index], 'g--', tm8a[:, 0], tm8a[:, index], 'r--', \
         tm2b[:, 0], tm2b[:, index], 'b-.', tm4b[:, 0], tm4b[:, index], 'g-.', tm8b[:, 0], tm8b[:, index], 'r-.', \
         ot3, ac2tm, 'b+', ot3, ac4tm, 'g+', ot3, ac8tm, 'r+')
plt.xlim([0, 70])
plt.ylim([0, 25])
plt.text(lx, ly, '(d6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

ot1 = [0, 15, 30, 60];
fe2co = [0.789,10.541, 10.198, 12.734]
fe4co = [0.789, 6.601, 12.568, 15.624]
fe8co = [0.789, 9.283, 16.091, 16.601]

offset = 24
index = 13
ax1=subplot(8, 6, 25);
ax1.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.', \
         ot1, fe2co, 'b+', ot1, fe4co, 'g+', ot1, fe8co, 'r+')
plt.xlim([0, 70])
plt.ylim([0, 100])
plt.yticks([0, 20, 40, 60, 80])
plt.ylabel('Fe(II) (mM)')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(e1)', transform=ax1.transAxes)

ax5=subplot(8, 6, 26);
fe2ro = [0.102, 7.30, 20.85, 23.76]
fe4ro = [0.102, 2.62, 19.51, 37.49]
fe8ro = [0.102, 2.34, 17.90, 31.31]
ax5.plot(ro2a[:, 0], ro2a[:, index], 'b--', ro4a[:, 0], ro4a[:, index], 'g--', ro8a[:, 0], ro8a[:, index], 'r--', \
         ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.', \
         ot1, fe2ro, 'b+', ot1, fe4ro, 'g+', ot1, fe8ro, 'r+')
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, 100])
plt.text(lx, ly, '(e2)', transform=ax5.transAxes)
plt.xlabel('Time (d)')

ax9=subplot(8, 6, 27);
fe2to = [15.67,25.36 , 32.26 , 27.82 ]
fe4to = [15.67,21.82 , 34.03 , 33.07 ]
fe8to = [15.67,16.05 , 28.07 , 34.15 ]
ax9.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b--', to4a[:, 0], to4a[:, index], 'g--', to8a[:, 0], to8a[:, index], 'r--', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.', \
         ot1, fe2to, 'b+', ot1, fe4to, 'g+', ot1, fe8to, 'r+')
#plt.ylabel('Fe(II) (mM)')
plt.xlim([0, 70])
plt.ylim([0, 100])
plt.text(lx, ly, '(e3)', transform=ax9.transAxes)
plt.setp(ax9.get_xticklabels(), visible=False)
plt.setp(ax9.get_yticklabels(), visible=False)

ax2=subplot(8, 6, 28);
fe2cm = [22.23,33.440, 109.22, 290.47]
fe4cm = [22.23,30.630,  75.63, 309.84]
fe8cm = [22.23,38.440,  57.34,  84.38]

ax2.plot(cm2a[:, 0], cm2a[:, index], 'b--', cm4a[:, 0], cm4a[:, index], 'g--', cm8a[:, 0], cm8a[:, index], 'r--', \
         cm2[:, 0], cm2[:, index], 'b-', cm4[:, 0], cm4[:, index], 'g-', cm8[:, 0], cm8[:, index], 'r-', \
         cm2b[:, 0], cm2b[:, index], 'b-.', cm4b[:, 0], cm4b[:, index], 'g-.', cm8b[:, 0], cm8b[:, index], 'r-.', \
         ot1, fe2cm, 'b+', ot1, fe4cm, 'g+', ot1, fe8cm, 'r+')
plt.xlim([0, 70])
plt.ylim([0, 100])
plt.text(lx, ly, '(e4)', transform=ax2.transAxes)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)

ax6=subplot(8, 6, 29);
fe2rm = [22.97,37.570,  44.19,  32.57]
fe4rm = [22.97,30.810,  44.05,  33.51]
fe8rm = [22.97,24.870,  43.78,  38.24]
ax6.plot(rm2[:, 0], rm2[:, index], 'b-', rm4[:, 0], rm4[:, index], 'g-', rm8[:, 0], rm8[:, index], 'r-', \
         rm2a[:, 0], rm2a[:, index], 'b--', rm4a[:, 0], rm4a[:, index], 'g--', rm8a[:, 0], rm8a[:, index], 'r--', \
         rm2b[:, 0], rm2b[:, index], 'b-.', rm4b[:, 0], rm4b[:, index], 'g-.', rm8b[:, 0], rm8b[:, index], 'r-.', \
         ot1, fe2rm, 'b+', ot1, fe4rm, 'g+', ot1, fe8rm, 'r+')
plt.xlim([0, 70])
plt.ylim([0, 100])
plt.text(lx, ly, '(e5)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

axa=subplot(8, 6, 30);
fe2tm = [ 7.18,23.040,  30.89,  44.81]
fe4tm = [ 7.18,21.140,  59.23,  33.80]
fe8tm = [ 7.18, 5.700,  50.89,  52.41]
axa.plot(tm2[:, 0], tm2[:, index], 'b-', tm4[:, 0], tm4[:, index], 'g-', tm8[:, 0], tm8[:, index], 'r-', \
         tm2a[:, 0], tm2a[:, index], 'b--', tm4a[:, 0], tm4a[:, index], 'g--', tm8a[:, 0], tm8a[:, index], 'r--', \
         tm2b[:, 0], tm2b[:, index], 'b-.', tm4b[:, 0], tm4b[:, index], 'g-.', tm8b[:, 0], tm8b[:, index], 'r-.', \
         ot1, fe2tm, 'b+', ot1, fe4tm, 'g+', ot1, fe8tm, 'r+')
plt.xlim([0, 70])
plt.ylim([0, 100])
plt.setp(axa.get_xticklabels(), visible=False)
plt.setp(axa.get_yticklabels(), visible=False)
plt.text(lx, ly, '(e6)', transform=axa.transAxes)

index = 20
ax1=subplot(8, 6,31);
ax1.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, 0.6])
plt.yticks([0, .2, .4])
plt.ylabel('FeRb (mM)')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(f1)', transform=ax1.transAxes)

ax2=subplot(8, 6,32);
ax2.plot(ro2a[:, 0], ro2a[:, index], 'b--', ro4a[:, 0], ro4a[:, index], 'g--', ro8a[:, 0], ro8a[:, index], 'r--', \
         ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, 0.6])
plt.text(lx, ly, '(f2)', transform=ax2.transAxes)

ax3=subplot(8, 6,33);
ax3.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b--', to4a[:, 0], to4a[:, index], 'g--', to8a[:, 0], to8a[:, index], 'r--', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, 0.6])
plt.text(lx, ly, '(f3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(8, 6,34);
ax4.plot(cm2a[:, 0], cm2a[:, index], 'b--', cm4a[:, 0], cm4a[:, index], 'g--', cm8a[:, 0], cm8a[:, index], 'r--', \
         cm2[:, 0], cm2[:, index], 'b-', cm4[:, 0], cm4[:, index], 'g-', cm8[:, 0], cm8[:, index], 'r-', \
         cm2b[:, 0], cm2b[:, index], 'b-.', cm4b[:, 0], cm4b[:, index], 'g-.', cm8b[:, 0], cm8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, 0.6])
plt.text(lx, ly, '(f4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(8, 6,35);
ax5.plot(rm2[:, 0], rm2[:, index], 'b-', rm4[:, 0], rm4[:, index], 'g-', rm8[:, 0], rm8[:, index], 'r-', \
         rm2a[:, 0], rm2a[:, index], 'b--', rm4a[:, 0], rm4a[:, index], 'g--', rm8a[:, 0], rm8a[:, index], 'r--', \
         rm2b[:, 0], rm2b[:, index], 'b-.', rm4b[:, 0], rm4b[:, index], 'g-.', rm8b[:, 0], rm8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, 0.6])
plt.text(lx, ly, '(f5)', transform=ax5.transAxes)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)

ax6=subplot(8, 6,36);
ax6.plot(tm2[:, 0], tm2[:, index], 'b-', tm4[:, 0], tm4[:, index], 'g-', tm8[:, 0], tm8[:, index], 'r-', \
         tm2a[:, 0], tm2a[:, index], 'b--', tm4a[:, 0], tm4a[:, index], 'g--', tm8a[:, 0], tm8a[:, index], 'r--', \
         tm2b[:, 0], tm2b[:, index], 'b-.', tm4b[:, 0], tm4b[:, index], 'g-.', tm8b[:, 0], tm8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, 0.6])
plt.text(lx, ly, '(f6)', transform=ax6.transAxes)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

index = 21
ax1=subplot(8, 6,37);
ax1.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.yticks([0, .01])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.text(lx, ly, '(g1)', transform=ax1.transAxes)
plt.ylabel('MeGAb (mM)')

ax2=subplot(8, 6,38);
ax2.plot(ro2a[:, 0], ro2a[:, index], 'b--', ro4a[:, 0], ro4a[:, index], 'g--', ro8a[:, 0], ro8a[:, index], 'r--', \
         ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.text(lx, ly, '(g2)', transform=ax2.transAxes)

ax3=subplot(8, 6,39);
ax3.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b--', to4a[:, 0], to4a[:, index], 'g--', to8a[:, 0], to8a[:, index], 'r--', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.text(lx, ly, '(g3)', transform=ax3.transAxes)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)

ax4=subplot(8, 6,40);
ax4.plot(cm2a[:, 0], cm2a[:, index], 'b--', cm4a[:, 0], cm4a[:, index], 'g--', cm8a[:, 0], cm8a[:, index], 'r--', \
         cm2[:, 0], cm2[:, index], 'b-', cm4[:, 0], cm4[:, index], 'g-', cm8[:, 0], cm8[:, index], 'r-', \
         cm2b[:, 0], cm2b[:, index], 'b-.', cm4b[:, 0], cm4b[:, index], 'g-.', cm8b[:, 0], cm8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.text(lx, ly, '(g4)', transform=ax4.transAxes)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

ax5=subplot(8, 6,41);
ax5.plot(rm2[:, 0], rm2[:, index], 'b-', rm4[:, 0], rm4[:, index], 'g-', rm8[:, 0], rm8[:, index], 'r-', \
         rm2a[:, 0], rm2a[:, index], 'b--', rm4a[:, 0], rm4a[:, index], 'g--', rm8a[:, 0], rm8a[:, index], 'r--', \
         rm2b[:, 0], rm2b[:, index], 'b-.', rm4b[:, 0], rm4b[:, index], 'g-.', rm8b[:, 0], rm8b[:, index], 'r-.')
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax5.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.text(lx, ly, '(g5)', transform=ax5.transAxes)

ax6=subplot(8, 6, 42);
ax6.plot(tm2[:, 0], tm2[:, index], 'b-', tm4[:, 0], tm4[:, index], 'g-', tm8[:, 0], tm8[:, index], 'r-', \
         tm2a[:, 0], tm2a[:, index], 'b--', tm4a[:, 0], tm4a[:, index], 'g--', tm8a[:, 0], tm8a[:, index], 'r--', \
         tm2b[:, 0], tm2b[:, index], 'b-.', tm4b[:, 0], tm4b[:, index], 'g-.', tm8b[:, 0], tm8b[:, index], 'r-.')
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.text(lx, ly, '(g6)', transform=ax6.transAxes)

index = 22
ax1=subplot(8, 6,43);
ax1.plot(co2[:, 0], co2[:, index], 'b-', co4[:, 0], co4[:, index], 'g-', co8[:, 0], co8[:, index], 'r-', \
         co2a[:, 0], co2a[:, index], 'b--', co4a[:, 0], co4a[:, index], 'g--', co8a[:, 0], co8a[:, index], 'r--', \
         co2b[:, 0], co2b[:, index], 'b-.', co4b[:, 0], co4b[:, index], 'g-.', co8b[:, 0], co8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.yticks([0, .01])
plt.xticks([0, 10, 20, 30, 40, 50, 60])
plt.text(lx, ly, '(h1)', transform=ax1.transAxes)
plt.ylabel('MeGHb (mM)')
plt.xlabel('Time (d)')

ax2=subplot(8, 6,44);
ax2.plot(ro2a[:, 0], ro2a[:, index], 'b--', ro4a[:, 0], ro4a[:, index], 'g--', ro8a[:, 0], ro8a[:, index], 'r--', \
         ro2[:, 0], ro2[:, index], 'b-', ro4[:, 0], ro4[:, index], 'g-', ro8[:, 0], ro8[:, index], 'r-', \
         ro2b[:, 0], ro2b[:, index], 'b-.', ro4b[:, 0], ro4b[:, index], 'g-.', ro8b[:, 0], ro8b[:, index], 'r-.')
plt.setp(ax2.get_yticklabels(), visible=False)
plt.xticks([0, 10, 20, 30, 40, 50, 60])
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.text(lx, ly, '(h2)', transform=ax2.transAxes)
plt.xlabel('Time (d)')

ax3=subplot(8, 6,45);
ax3.plot(to2[:, 0], to2[:, index], 'b-', to4[:, 0], to4[:, index], 'g-', to8[:, 0], to8[:, index], 'r-', \
         to2a[:, 0], to2a[:, index], 'b--', to4a[:, 0], to4a[:, index], 'g--', to8a[:, 0], to8a[:, index], 'r--', \
         to2b[:, 0], to2b[:, index], 'b-.', to4b[:, 0], to4b[:, index], 'g-.', to8b[:, 0], to8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.xticks([0, 10, 20, 30, 40, 50, 60])
plt.text(lx, ly, '(h3)', transform=ax3.transAxes)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')

ax4=subplot(8, 6,46);
ax4.plot(cm2a[:, 0], cm2a[:, index], 'b--', cm4a[:, 0], cm4a[:, index], 'g--', cm8a[:, 0], cm8a[:, index], 'r--', \
         cm2[:, 0], cm2[:, index], 'b-', cm4[:, 0], cm4[:, index], 'g-', cm8[:, 0], cm8[:, index], 'r-', \
         cm2b[:, 0], cm2b[:, index], 'b-.', cm4b[:, 0], cm4b[:, index], 'g-.', cm8b[:, 0], cm8b[:, index], 'r-.')
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.xticks([0, 10, 20, 30, 40, 50, 60])
plt.text(lx, ly, '(h4)', transform=ax4.transAxes)
plt.setp(ax4.get_yticklabels(), visible=False)
plt.xlabel('Time (d)')

ax5=subplot(8, 6,47);
ax5.plot(rm2[:, 0], rm2[:, index], 'b-', rm4[:, 0], rm4[:, index], 'g-', rm8[:, 0], rm8[:, index], 'r-', \
         rm2a[:, 0], rm2a[:, index], 'b--', rm4a[:, 0], rm4a[:, index], 'g--', rm8a[:, 0], rm8a[:, index], 'r--', \
         rm2b[:, 0], rm2b[:, index], 'b-.', rm4b[:, 0], rm4b[:, index], 'g-.', rm8b[:, 0], rm8b[:, index], 'r-.')
plt.setp(ax5.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.xticks([0, 10, 20, 30, 40, 50, 60])
plt.text(lx, ly, '(h5)', transform=ax5.transAxes)
plt.xlabel('Time (d)')

ax6=subplot(8, 6, 48);
ax6.plot(tm2[:, 0], tm2[:, index], 'b-', tm4[:, 0], tm4[:, index], 'g-', tm8[:, 0], tm8[:, index], 'r-', \
         tm2a[:, 0], tm2a[:, index], 'b--', tm4a[:, 0], tm4a[:, index], 'g--', tm8a[:, 0], tm8a[:, index], 'r--', \
         tm2b[:, 0], tm2b[:, index], 'b-.', tm4b[:, 0], tm4b[:, index], 'g-.', tm8b[:, 0], tm8b[:, index], 'r-.')
plt.setp(ax6.get_yticklabels(), visible=False)
plt.xlim([0, 70])
plt.ylim([0, .02])
plt.text(lx, ly, '(h6)', transform=ax6.transAxes)
plt.xlabel('Time (d)')

plt.subplots_adjust(left=0.06, right=0.98, top=0.95, bottom=0.05)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(15, 12)
savefig('plot3c.pdf')
#show()
