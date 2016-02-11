set terminal postscript eps size 8, 8 enhanced color font 'Helvetica, 20' lw 1 
set output 'ex4a.eps'
set style line 1 lt 1 lw 3 lc rgb "blue"
set style line 2 lt 1 lw 3 lc rgb "red"

set multiplot layout 3, 2 rowsfirst

set label 1 '(a)' at graph 0.05, graph 0.9 
set xrange[0:20]
set yrange[0:1.2]
#set xlabel 'Time [d]' 
set ylabel 'Acetate [mM]' 
plot 'ex3c.txt' using 1:3 title 'Catabolic' with lines ls 1, \
     'ex4a.txt' using 1:3 title 'Anabolic' with lines ls 2 

set nokey
set label 1 '(b)' at graph 0.05, graph 0.9
set xrange[0:20]
set yrange[19:20.2]
#set xlabel 'Time [d]' 
set ylabel 'Sulfate [mM]' 
plot 'ex3c.txt' using 1:4 title 'Sulfate' with lines ls 1, \
     'ex4a.txt' using 1:4 title 'Sulfate' with lines ls 2

set label 1 '(c)' at graph 0.05, graph 0.9 
set xrange[0:20]
set yrange[5:10]
#set xlabel 'Time [d]' 
set ylabel 'pH' 
plot 'ex3c.txt' using 1:2 title 'pH' with lines ls 1, \
     'ex4a.txt' using 1:2 title 'pH' with lines ls 2

set label 1 '(d)' at graph 0.05, graph 0.9 
set xrange[0:20]
set yrange[-500:500]
#set xlabel 'Time [d]' 
set ylabel 'SI(SRA)' 
plot 'ex4a.txt' using 1:6 title 'F_T' with lines ls 2

set label 1 '(e)' at graph 0.05, graph 0.9 
set xrange[0:20]
set yrange[0:5]
set xlabel 'Time [d]' 
set ylabel 'Sulfate reducer [mg/L]' 
plot 'ex3c.txt' using 1:5 title 'SRB' with lines ls 1, \
     'ex4a.txt' using 1:5 title 'SRB' with lines ls 2

set label 1 '(f)' at graph 0.05, graph 0.9 
set xrange[0:20]
set yrange[0:0.5]
set xlabel 'Time [d]' 
set ylabel 'Rate [mM/d]' 
plot 'ex3c.txt' using 1:7 title 'Rate' with lines ls 1, \
     'ex4a.txt' using 1:($7*24.9522) title 'Rate' with lines ls 2

unset multiplot
