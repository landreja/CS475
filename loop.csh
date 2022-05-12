#!/bin/csh

foreach n ( 1000 10000 62500 125000 250000 500000 1000000 2000000 4000000 8000000 ) 

    g++ proj04.cpp -DARRAYSIZE=$t -o project4 -fopenmp 

./project4 

end

