import sys
import pandas as pd

# csv file with data:
# in terminal, fixed the changed ',' to '.' and then ';' to ','
# cat NMR_for_python.csv | sed s/,/./g | sed s/\;/,/g > NMR_for_python_fixed.csv

f = sys.argv[1]
p = float(sys.argv[2])  # cutoff for t-test (use 0.01 as default)

NMRdata = pd.read_csv(f)  # 'NMR_for_python_fixed.csv'
NMR_df = pd.DataFrame(NMRdata)   # csv -> df
NMR_df = NMR_df.drop([0], axis=0)   # drop extra header row

# Make new dfs for temperature (column Temp) 4 degrees and 25 degrees.
Temp4 = NMR_df.loc[NMR_df['Temp'] == '4']
Temp25 = NMR_df.loc[NMR_df['Temp'] == '25']

# Check the indices of the columns to be used

def col_index(df, col_name):
    i_col_name = df.columns.get_loc(col_name)
    return i_col_name


# Check which indices should be used for dividing the dataframe
i_shift1 = col_index(NMR_df, "Shift1")
i_shiftC1 = col_index(NMR_df, "ShiftC1")
i_shiftLast = len(NMR_df.columns)

# Keep only data from NMR shifts in df and divide into uncorrected and corrected data
Temp4_uncorr = Temp4.iloc[:, i_shift1:i_shiftC1]
Temp4_corr = Temp4.iloc[:, i_shiftC1:i_shiftLast]
Temp25_uncorr = Temp25.iloc[:, i_shift1:i_shiftC1]
Temp25_corr = Temp25.iloc[:, i_shiftC1:i_shiftLast]

# Is difference significant between same column sets of values for 4 and 25 degrees? Use paired t-test:
# Use the TempX_(un)corr dfs from above. Compare 4 degrees to 25 degrees

def sign_diff_check(df1, df2, cutoff): # Checks if the column-wise difference of the mean values in two dataframes is significant
    if len(df1.columns) != len(df2.columns):  # number of columns have to be the same
        print("")
        print("Dataframes do not have the same number of columns!")
        print("")
    else:
        from scipy import stats
        col_list = []
        for column in df1.columns:
            col_values1 = df1[column]
            col_values2 = df2[column]
            t_check = stats.ttest_ind(col_values1, col_values2)
            if t_check.pvalue < cutoff:
                col_list.append(column)
    return col_list


# Get the list of columns that showed significant difference between 4 and 25 degrees
sign_diff_uncorr = sign_diff_check(Temp4_uncorr, Temp25_uncorr, p)  # a list of column names
print("Number of NMR shifts that differ significantly for 4 and 25 degrees (uncorrected values):")
print(len(sign_diff_uncorr))
print("Column names:")
print(sign_diff_uncorr)

sign_diff_corr = sign_diff_check(Temp4_corr, Temp25_corr, p)
print("NMR shifts that differ significantly for 4 and 25 degrees (corrected values):")
print(len(sign_diff_corr))
print("Column names:")
print(sign_diff_corr)

# ---------------------- STOP HERE -------------------------------

# Analyze distribution properties and compare 4 and 25 to each other
#    Box plot values?

# Compare a test sample to the values in the columns with significant difference
# How? "Closest to" for each mean value for each column?

# Use function mean() to use on a dataframe to get means of all significant columns
# Calculate the mean value of all columns (axis=0 means adding the row elements)
#####T4u_means = Temp4_uncorr.loc[sign_diff_uncorr].mean(axis=0)
#T4c_means = Temp4_corr.mean(axis=0)
#T25u_means = Temp25_uncorr.mean(axis=0)
#T25c_means = Temp25_corr.mean(axis=0)



#def closest_to()

# Decide on cutoff values for: (can it be baked into function below?)
#    rt
#    probably rt
#    Uncertain
#    probably 4 degrees
#    4 degrees
#    (Note: rt and 4 degrees does not have to exist as options for all shifts)

#    More in detail:
#    For each shift
#        Make new empty list named according to shift
#        For each sample
#            (something that compares the two distributions and decides on cutoffs)
#        Append to list with cutoff values





