set terminal postscript eps size 8, 8 enhanced color font 'Helvetica, 20' lw 1 
set output 'ex3c.eps'
set style line 1 lt 1 lw 3 lc rgb "blue"
set style line 2 lt 1 lw 3 lc rgb "red"
set style line 3 lt 1 lw 3 lc rgb "green"
set style line 4 lt 1 lw 3 lc rgb "violet"

set multiplot layout 3, 2 rowsfirst

set label 1 '(a)' at graph 0.05, graph 0.9 
set xrange[0:20]
set yrange[0:1.2]
#set xlabel 'Time [d]' 
set ylabel 'Acetate [mM]' 
plot 'ex3.txt' using 1:3 title 'Case 1' with lines ls 1, \
     'ex3a.txt' using 1:3 title 'Case 2' with lines ls 2, \
     'ex3b.txt' using 1:3 title 'Case 3' with lines ls 3, \
     'ex3c.txt' using 1:3 title 'Case 4' with lines ls 4 

set nokey
set label 1 '(b)' at graph 0.05, graph 0.9
set xrange[0:20]
set yrange[19:20.2]
#set xlabel 'Time [d]' 
set ylabel 'Sulfate [mM]' 
plot 'ex3.txt' using 1:4 title 'Sulfate' with lines ls 1, \
     'ex3a.txt' using 1:4 title 'Sulfate' with lines ls 2, \
     'ex3b.txt' using 1:4 title 'Sulfate' with lines ls 3, \
     'ex3c.txt' using 1:4 title 'Sulfate' with lines ls 4

set label 1 '(c)' at graph 0.05, graph 0.9 
set xrange[0:20]
set yrange[5:10]
#set xlabel 'Time [d]' 
set ylabel 'pH' 
plot 'ex3.txt' using 1:2 title 'pH' with lines ls 1, \
     'ex3a.txt' using 1:2 title 'pH' with lines ls 2, \
     'ex3b.txt' using 1:2 title 'pH' with lines ls 3, \
     'ex3c.txt' using 1:2 title 'pH' with lines ls 4

set label 1 '(d)' at graph 0.05, graph 0.9 
set xrange[0:20]
set yrange[0:1]
#set xlabel 'Time [d]' 
set ylabel 'F_T' 
plot 'ex3.txt' using 1:6 title 'F_T' with lines ls 1, \
     'ex3a.txt' using 1:6 title 'F_T' with lines ls 2, \
     'ex3b.txt' using 1:6 title 'F_T' with lines ls 3, \
     'ex3c.txt' using 1:6 title 'F_T' with lines ls 4

set label 1 '(e)' at graph 0.05, graph 0.9 
set xrange[0:20]
set yrange[0:5]
set xlabel 'Time [d]' 
set ylabel 'Sulfate reducer [mg/L]' 
plot 'ex3.txt' using 1:5 title 'SRB' with lines ls 1, \
     'ex3a.txt' using 1:5 title 'SRB' with lines ls 2, \
     'ex3b.txt' using 1:5 title 'SRB' with lines ls 3, \
     'ex3c.txt' using 1:5 title 'SRB' with lines ls 4

set label 1 '(f)' at graph 0.05, graph 0.9 
set xrange[0:20]
set yrange[0:0.25]
set xlabel 'Time [d]' 
set ylabel 'Rate [mM/d]' 
plot 'ex3.txt' using 1:7 title 'Rate' with lines ls 1, \
     'ex3a.txt' using 1:7 title 'Rate' with lines ls 2, \
     'ex3b.txt' using 1:7 title 'Rate' with lines ls 3, \
     'ex3c.txt' using 1:7 title 'Rate' with lines ls 4

unset multiplot
