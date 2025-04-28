set boxwidth 0.5
set datafile separator ","
set style fill solid
set yrange [0:50000]
set xrange [0:2]
set xlabel 'proxy'
set ylabel 'calls'
set tics font ",10"
plot "proxy.csv" using 1:2:xtic(1) with boxes
