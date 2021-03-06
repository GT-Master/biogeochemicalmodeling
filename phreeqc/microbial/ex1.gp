reset
set style line 1 lt 1 lw 5 lc rgb "blue"
set style line 2 lt 1 lw 5 lc rgb "red"
set style line 3 lt 1 lw 5 lc rgb "green"
set style line 4 lt 1 lw 5 lc rgb "violet"
set xrange[0:20]
set yrange[0:2]
set y2range[6:10]
set xlabel 'Time [d]' 
set ylabel 'Concentration [mM]' 
set y2label 'pH' 
set y2tics 6, 1, 10
plot \
     'ex1.txt' using ($1/3600/24):($3*1000) title 'Acetate' with lines ls 1 axes x1y1, \
     'ex1.txt' using ($1/3600/24):($4*1000) title 'Sulfate' with lines ls 2 axes x1y1, \
     'ex1.txt' using ($1/3600/24):($5*1000) title 'Sulfide' with lines ls 3 axes x1y1, \
     'ex1.txt' using ($1/3600/24):($2) title 'pH' with lines ls 4 axes x1y2
set terminal postscript eps size 4, 3 enhanced color font 'Helvetica, 20' lw 1 
set output 'ex1.eps'
replot
set xterm pop
pause -1


