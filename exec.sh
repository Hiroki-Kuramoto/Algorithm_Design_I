#!/bin/bash
echo ----- start tableMaker -----
time python tableMaker.py
echo ----- start exhaustiveSearch -----
time python exhaustiveSearch.py
echo ----- start dpSearch -----
time python dpSearch.py
