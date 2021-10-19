# NMR data manipulation

  * Takes raw data from an NMR experiment and pairwise compares all samples stored at 4 degrees C with all samples stored at 25 degrees C. A paired t-test is    performed, and the column names where the mean values differ significantly between the two temperatures are returned, together with the number of columns.

# How to run

  * python csv_file cutoff
  * Comment: use 0.01 as default p-value cutoff

# Arguments
  
  * Arg1: csv file
  * Arg2: p-value cutoff

# Example
  
  * python my_file.csv 0.01
  
  
