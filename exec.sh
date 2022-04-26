#!/bin/bash

python tableMaker.py

start_time=`date +%s`

python exhaustiveSearch.py

end_time=`date +%s` 
run_time=$((end_time - start_time))
echo exhaustiveSearch = $run_time sec

start_time=`date +%s`

python dpSearch.py

end_time=`date +%s` 
run_time=$((end_time - start_time))
echo subsetSum = $run_time sec