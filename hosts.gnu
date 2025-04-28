set boxwidth 0.5
set datafile separator ","
set style fill solid 
set yrange [1980:2010]
set xrange [0:49]
set xlabel 'host'
set ylabel 'calls'
set tics font ",4"
plot "hosts.csv" using 1:2:xtic(1) with boxes fc 'blue'
