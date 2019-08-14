# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## There are alternative solution and hits: 
# ### more readable
# > 10, 18, 23, 24, 25, 28, 37, 38, 44, 54, 58, 60
# ### more effient (vectorlized)
# > 16, 19, 24, 43
# ### when to use it?
# > 13, 26, 36, 39, 41, 58, 60,
# ### hints
# > 12, 18, 22, 24, 28, 29, 30, 33, 56, 59

import pandas as pd

# 1. How to import pandas and check the version? 
print(pd.__version__)
print(pd.show_versions(as_json=True))

# +
# 2. How to create a series from a list, numpy array and dict?
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)

# +
# 3. How to convert the index of a series into a column of a dataframe?
# L1
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

df = ser.to_frame().reset_index()
df.head()

# +
# 4. How to combine many series to form a dataframe?
# L1
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.concat([ser1, ser2], axis=1)
df.head()

# +
# 5. How to assign name to the series’ index?
# L1
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))

ser.name = 'alphabets'

# +
# 6. How to get the items of series A not present in series B?
# L2
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

mask = ~ ser1.isin(ser2)
ser1[mask]

# +
# 7. How to get the items not common to both series A and series B?
# L2
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

union_ser = pd.Series(np.union1d(ser1, ser2))
intersection_ser = pd.Series(np.intersect1d(ser1, ser2))
xor_ser = union_ser[~ union_ser.isin(intersection_ser)]
xor_ser
# -

# 8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
# L2
ser = pd.Series(np.random.normal(10, 5, 25))
ser.quantile([.0, .25, .5, .75, 1])

# 9. How to get frequency counts of unique items of a series?
#  L1
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser.value_counts()

# +
# 10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?
# L2
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

# ALTERNATIVE ANSWER
# More Readable
top_2_frequent = ser.value_counts().nlargest(2).index
ser.where(ser.isin(top_2_frequent), other='Other')
# -

#  11. How to bin a numeric series to 10 groups of equal size?
#  L2
ser = pd.Series(np.random.random(20))
# Note ourput dtype is category
pd.qcut(ser,
        q = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1],
        labels=['1st', '2nd','3rd','4th','5th',
                 '6th', '7th', '8th','9th', '10th'])

# +
# 12. How to convert a numpy array to a dataframe of given shape? (L1)
# L1
ser = pd.Series(np.random.randint(1, 10, 35))

# note : argument -1 will caculate the rest 
# in this case (7, -1) -->  (7 , 35 / 7)
pd.DataFrame(ser.values.reshape(7,-1))

# +
# 13. How to find the positions of numbers that are multiples of 3 from a series?
# L2
ser = pd.Series(np.random.randint(1, 10, 7))

# note : np.where, pd.where return whole series
#        np.argwhere return index
#        use the indrx :  arr = np.argwhere(ser condition), ser.iloc(arr.reshape(-1))
np.argwhere(ser % 3 == 0)

# +
# 14. How to extract items at given positions from a series
# L1
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

ser.iloc[pos]

# +
# 15. How to stack two series vertically and horizontally ?
# Difficulty Level: L1
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

df1 = pd.concat([ser1,ser2], axis=0).to_frame()
df2 = pd.concat([ser1,ser2], axis=1)

# +
# 16. How to get the positions of items of series A in another series B?
# Difficulty Level: L2
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])

# note : this solution is vectorlized
# faster than list comprehemsion for i in ser2 
# when data is big
np.argwhere(ser1.isin(ser2)).reshape(-1).tolist()
# + {}
# 17. How to compute the mean squared error on a truth and predicted series?
# Difficulty Level: L2
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)

print((truth - pred).pow(2).sum() / len(truth))
print(np.mean((truth - pred) ** 2))

# +
# 18. How to convert the first character of each element in a series to uppercase?
# Difficulty Level: L2
ser = pd.Series(['how', 'to', 'kick', 'ass?'])

# More readable
ser.str.capitalize()
# Hints
# you can use dir() to get all the method inside ser.str
# Now you could faster understand how ser.str can do
# print(dir(ser.str))

# +
# 19. How to calculate the number of characters in each word in a series?
# Difficulty Level: L2
ser = pd.Series(['how', 'to', 'kick', 'ass?'])

# vectorlzied

ser.str.len()

# +
# 20. How to compute difference of differences between consequtive numbers of a series?
# Difficulty Level: L1
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])

# Solition 1
tmp = ser.shift(1)
middle_result = ser - tmp
print(middle_result.tolist())
tmp2 = middle_result.shift(1)
print((middle_result - tmp2).tolist())

# Solution 2
print('-'*60)
print(ser.diff().tolist())
print(ser.diff().diff().tolist())
# + {}
# 21. How to convert a series of date-strings to a timeseries?
# Difficiulty Level: L2

ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])

pd.to_datetime(ser, infer_datetime_format=True)

# +
# 22. How to get the day of month, week number, day of year and day of week from a series of date strings?
# Difficiulty Level: L2

ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])

tmp = pd.to_datetime(ser)
# hint
# use dir(tmp.dt) to check it out what could be called
# tmp.dt is pandas.core.indexes.accessors.DatetimeProperties object
# use dir(tmp[0]) to check it out what could be called 
# tmp[0] is a single element, <class 'pandas._libs.tslibs.timestamps.Timestamp'>
# you might wanna to check
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html
# for Timestamp documentation
# https://dateutil.readthedocs.io/en/stable/index.html
# dateutil, really good when we want to dealing with time


Date = tmp.dt.day.tolist()
Week_number = tmp.dt.weekofyear.tolist()
Day_num_of_year = tmp.dt.dayofyear.tolist()
Dayofweek = tmp.dt.weekday_name.tolist()

print(f''' 
Date : {Date}
Week number : {Week_number}
Day num of year : {Day_num_of_year}
Day of week : {Dayofweek}
''')


# +
# 23. How to convert year-month string to dates corresponding to the 4th day of the month?
# Difficiulty Level: L2
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])

# ALTERNATIVE SOLUTION
# more readable
pd.to_datetime(ser, infer_datetime_format=True)

# +
# 24. How to filter words that contain atleast 2 vowels from a series?
# Difficiulty Level: L3

ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])

# ALTERNATIVE SOLUTION
# more readable
# vectorlized
condition = ser.str.count('[aeiouAEIOU]') >= 2
ser[condition]
# Hint, you cloud use print(dir(ser.str)) to check it out what could be called

# -

# * hint
#     * <img src = "./RegExp_snap.png"></img>
#     * pandas中的Series.str方法是向量化的，且通常都支援正則表達式(RegExp)
#     * 正則表達式可以幫助我們處理很多文字問題
#     * 像圖中的[aeiou]搭配[AEIUO] --> [aeiuoAEIUO]就解決了此題
#     * 或許你會想看看這份在[菜鳥上的教學](http://www.runoob.com/python/python-reg-expressions.html)


# +
# 25. How to filter valid emails from a series?
# Difficiulty Level: L3

# Extract the valid emails from the series emails. The regex pattern for valid emails is provided as reference.

emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'

# More readable
condition = emails.str.contains(pattern)
emails[condition].tolist()

# +
# 26. How to get the mean of a series grouped by another series?
# Difficiulty Level: L2
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
print(weights.tolist())
print(fruit.tolist())

print()
print(weights.groupby(fruit).mean())

# ALTERNATIVE SULOTION
tmp = pd.DataFrame({'fruit':fruit, 
              'weights':weights}).groupby('fruit').mean()

tmp['weights'].index.name = ''
print(tmp['weights'])

# When to use?
# 操作dataframe時我們通常都直接在dataframe裡面groupby, 這題告訴我們
# series 可以 groupby 另一條series, 之間用index作為對應, 
# 這讓feature engineering時能夠有更好的彈性
# + {}
# 27. How to compute the euclidean distance between two series?
# Difficiulty Level: L2

p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

sum((p - q) ** 2) ** 0.5


# +
# 28. How to find all the local maxima (or peaks) in a numeric series?
# Difficiulty Level: L3

# Get the positions of peaks (values surrounded by smaller values on both sides) in ser.

ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])

# more readable
peak_locs = np.argwhere(np.sign(ser.diff(1)) +\
                        np.sign(ser.diff(-1)) == 2).reshape(-1) 

# hint
# use diff(-1) to get the backforwd diff
# you could use this when using diff, shift function
# diff
peak_locs

# +
# 29. How to replace missing spaces in a string with the least frequent character?
# Replace the spaces in my_str with the least frequent character.

# Difficiulty Level: L2

# hint 
# a way to concant all series strnig 
ser = pd.Series(list('dbc deb abed gade'))
freq = ser.value_counts()
print(freq)
least_freq = freq.dropna().index[-1]
result = "".join(ser.replace(' ', least_freq))
print(result)

# ALTERNATIVE SOLUTION
my_str = 'dbc deb abed gade'

least_freq_character = pd.Series(list(my_str)).value_counts().index[-1]

my_str.replace(' ', least_freq_character)


# +
# 30. How to create a TimeSeries starting ‘2000-01-01’ and 10 weekends (saturdays) after that having random numbers as values?
# Difficiulty Level: L2
dateime_idx = pd.date_range('2000-01-01', periods=10, freq='W-SAT')

pd.Series(index = dateime_idx,
          data = np.random.randint(2,8,size=len(dateime_idx)))
# hint 
# it is really hard to find the pd.date_range method in documentation
# here is the documentation
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html


# +
# 31. How to fill an intermittent time series so all missing dates show up with values of previous non-missing date?
# Difficiulty Level: L2

ser = pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))

# Fill the datetime index using resample + ffill()
ser.resample('D').ffill()


# +
# 32. How to compute the autocorrelations of a numeric series?
# Difficiulty Level: L3

# Compute autocorrelations for the first 10 lags of ser. Find out which lag has the largest correlation.

ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))

# ALTERNATIVE　SOLUTION
tmp = pd.Series([abs(ser.autocorr(lag)) for lag in range(1,11)])
tmp.sort_values(ascending=False).head(1)

# +
# 33. How to import only every nth row from a csv file to create a dataframe?
# Difficiulty Level: L2

# Import every 50th row of BostonHousing dataset as a dataframe.
url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'

# df_result = pd.DataFrame()

df = pd.read_csv(url, chunksize=50)

df_result = pd.concat([chunk.iloc[0] for chunk in df], axis=1)

df_result.T
# Hint
# pd.read_csv(**param, chunksize=50)
# will return a TextFileReader 
# you can use that for looping
# you could see using
# print(type(df))


# +
# 34. How to change column values when importing csv to a dataframe?
# Difficulty Level: L2

# Import the boston housing dataset, but while importing change the 'medv' (median house value) column so that values < 25 becomes ‘Low’ and > 25 becomes ‘High’.

url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
converters = {'medv': lambda x :'High' if float(x) > 25
                                       else 'Low'}
df = pd.read_csv(url, converters=converters)
df.head()



# +
# 35. How to create a dataframe with rows as strides from a given series?
# Difficiulty Level: L3

L = pd.Series(range(15))

def gen_strides(a, stride_len=5, window_len=5):
    n_strides = ((a.size-window_len)//stride_len) + 1
    return np.array([a[s:(s+window_len)] for s in np.arange(0, a.size, stride_len)[:n_strides]])

gen_strides(L, stride_len=2, window_len=4)

# +
# 36. How to import only specified columns from a csv file?
# Difficulty Level: L1

url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
cols = ['crim','medv']
pd.read_csv(url, usecols=cols).head()

# When to use
# 資料量大時，硬體記憶體不足，只讀取幾個column做特徵工程
# 並存取特徵結果

# +
# 37. How to get the nrows, ncolumns, datatype, summary stats of each column of a dataframe? Also get the array and list equivalent.
# Difficulty Level: L2
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)

# More readable
display(
df.shape,
df.dtypes,
df.describe()
)
# get np.array and list
array = df.values
df_list = df.values.tolist()


# +
# 38. How to extract the row and column number of a particular cell with given criterion?
# Difficulty Level: L1

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# More Readable
highest_price = df['Price'].max()
# the dataframe rows
df.query(f'Price == {highest_price}')
# the row idx and col idx
row, col = np.argwhere(df.values == np.max(df.Price)).reshape(-1)
print(row, col)
# + {}
# 39. How to rename a specific columns in a dataframe?
# Difficulty Level: L2

# Rename the column Type as CarType in df and replace the ‘.’ in column names with ‘_’.
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

tmp = [col.replace('.','_') for col in df.columns]
df.columns = tmp
df = df.rename(columns={'Type':'CarType'})
df.columns

# When to use
# 第一次拿到資料時，針對特徵欄位做資料清理
# 甚至會加註categorical feature CAT_FeatureName
# Numerical feature Num_FeatureName......等


# +
# 40. How to check if a dataframe has any missing values?
# Difficulty Level: L1
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df.isnull().any().any()

# +
# 41. How to count the number of missing values in each column?
# Difficulty Level: L2
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

nan_p_series = df.isnull().sum() / len(df)
nan_p_series.sort_values(ascending=False).head(1)

# when to use
# 缺失值統計，近乎每次必用

# +
# 42. How to replace missing values of multiple numeric columns with the mean?
# Difficulty Level: L2

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

for col in ['Min.Price','Max.Price']:
    respective_mean = df[col].mean()
    df[col] = df[col].fillna(respective_mean)

df[['Min.Price','Max.Price']].isnull().any().any()

# +
# 43. How to use apply function on existing columns with global variables as additional arguments?
# Difficulty Level: L3

# In df, use apply method to replace the missing values in Min.Price with the column’s mean and those in Max.Price with the column’s median.

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

d = {'Min.Price': np.nanmean, 'Max.Price': np.nanmedian}
df[['Min.Price', 'Max.Price']] = df[['Min.Price', 'Max.Price']]\
.apply(lambda x, d: x.fillna(d[x.name](x)), args=(d, ))

# Vectorlized 
# 使用 42題的方式，改成median填入，是向量化操作
# 在資料量大時會快非常多

# +
# 44. How to select a specific column from a dataframe as a dataframe instead of a series?
# Difficulty Level: L2

df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

# More readable

df[['a']]

# +
# 45. How to change the order of columns of a dataframe?
# Difficulty Level: L3
# Actually 3 questions.

# In df, interchange columns 'a' and 'c'.
# Create a generic function to interchange two columns, without hardcoding column names.

# Sort the columns in reverse alphabetical order, that is colume 'e' first through column 'a' last.

df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

# 1
df[list('cbade')]

# 2 
# no function to do that
def swap_col(df, col1, col2):
    df_swap = df.copy()
    col_list = list(df_swap.columns)
    col1_idx = col_list.index(col1)
    col2_idx = col_list.index(col2)
    col_list[col1_idx] = col2
    col_list[col2_idx] = col1
    
    return df_swap[col_list]

swap_col(df, 'c','e')

# 3
new_order = sorted(list(df.columns), reverse=True)
df[new_order]

# +
# 46. How to set the number of rows and columns displayed in the output?
# Difficulty Level: L2

# Change the pamdas display settings on printing the dataframe df it shows a maximum of 10 rows and 10 columns.

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# show all options
# pd.describe_option()
pd.set_option('display.max_columns', 10) 
pd.set_option('display.max_rows', 10) 
df
# -
pd.describe_option()

# +
# 47. How to format or suppress scientific notations in a pandas dataframe?
# Difficulty Level: L2

# Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])


pd.options.display.float_format = '{:,.4f}'.format

display(df)

# undo
pd.options.display.float_format = None


# +
# 48. How to format all the values in a dataframe as percentages?
# Difficulty Level: L2

# Format the values in column 'random' of df as percentages.

df = pd.DataFrame(np.random.random(4), columns=['random'])


df.style.format({'random':'{0:.2%}'.format,})

# +
# 49. How to filter every nth row in a dataframe?
# Difficulty Level: L1

# From df, filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# More readable

idx = np.arange(0, df.shape[0], step=20)
col = ['Manufacturer','Model','Type']
df[col].iloc[idx]

# +
# 50. How to create a primary key index by combining relevant columns?
# Difficulty Level: L2

# In df, Replace NaNs with ‘missing’ in columns 'Manufacturer', 'Model' and 'Type' 
# and create a index as a combination of these three columns and check if the index is a primary key.

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv', usecols=[0,1,2,3,5])

col = ['Manufacturer','Model','Type']
idx_col = '.Price'
df[col] = df[col].fillna('missing')
df.index = df.Manufacturer + '_' + df.Model + '_' + df.Type
display(df.head(),
       df.index.is_unique)
# When to use
# 根據column內容來設置 Primary key的手法非常實用
# 容易給其他同事進行表格閱讀

# +
# 51. How to get the row number of the nth largest value in a column?
# Difficulty Level: L2
# Find the row position of the 5th largest value of column 'a' in df.
df = pd.DataFrame(np.random.randint(1, 30, 30).reshape(10,-1), columns=list('abc'))

# More readable

df['a'].nlargest().index[-1]

# +
# 52. How to find the position of the nth largest value greater than a given value?
# Difficulty Level: L2

# In ser, find the position of the 2nd largest value greater than the mean.

# More readable
ser = pd.Series(np.random.randint(1, 100, 15))

tmp = ser - ser.mean()

tmp.nlargest(2).index

# +
# 53. How to get the last n rows of a dataframe with row RowSum > 100?
# Difficulty Level: L2

# Get the last two rows of df whose row RowSum is greater than 100.
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

# More readable
df['RowSum'] = df.sum(axis=1)
df.query('RowSum > 100').tail(2)
# + {}
# 54. How to find and cap outliers from a series or dataframe column?
# Difficulty Level: L2

# Replace all values of ser in the lower 5%ile and greater than 95%ile with respective 5th and 95th %ile value.

# More readable
ser = pd.Series(np.logspace(-2, 2, 30))
low = np.quantile(ser, q=.05)
high = np.quantile(ser, q=.95)
ser.clip(low, high)


# +
# 55. How to reshape a dataframe to the largest possible square after removing the negative values?

# Difficulty Level: L3

# Reshape df to the largest possible square with negative values removed.
# Drop the smallest values if need be. 
# The order of the positive numbers in the result should remain the same as the original.

df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))
display(df)
def larget_square(df):
    tmp = df.copy()
    # get positive array
    arr = tmp[tmp > 0].values
    arr = arr[~ np.isnan(arr)]
    # get largest square of side
    N = np.floor(arr.shape[0] ** 0.5).astype(int)
    # get index the arr soted
    top_idx = np.argsort(arr)[::-1]
    # drop min idx satisfied largest square
    # then reshape
    # key point, sort the top_idx, will give us 
    # the original idx already take out minmimum value
    filtered_idx = top_idx[: (N ** 2)]
    result = pd.DataFrame(arr[sorted(filtered_idx)].reshape(N, -1))
    return result

larget_square(df)

# +
# 56. How to swap two rows of a dataframe?
# Difficulty Level: L2

# Swap rows 1 and 2 in df.

df = pd.DataFrame(np.arange(25).reshape(5, -1))
display(df.head(2))
row1, row2 = df.iloc[0].copy(), df.iloc[1].copy()
df.iloc[0], df.iloc[1] = row2, row1
display(df.head(2))

# Hint
# use copy, or you're chaining by the original dataframe

# +
# 57. How to reverse the rows of a dataframe?
# Difficulty Level: L2

# Reverse all the rows of dataframe df.

df = pd.DataFrame(np.arange(25).reshape(5, -1))

df.iloc[::-1]

# +
# 58. How to create one-hot encodings of a categorical variable (dummy variables)?
# Difficulty Level: L2

# Get one-hot encodings for column 'a' in the dataframe df and append it as columns.

df = pd.DataFrame(np.arange(25).reshape(5,-1), columns=list('abcde'))

# More readable
concat_list = [df.drop(columns=['a']),
              pd.get_dummies(df['a'])]

result = pd.concat(concat_list, axis=1)
result

# When to use
# one hot encoding 非常常用, 其中get_dummy有sparse, drop_first可以選
# 但testing set 或是 validation set 出現unseen column 需要進行處理
# 推薦使用 sklearn.preprocessing, unseen col會使training col 全為0
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html


# +
# 59. Which column contains the highest number of row-wise maximum values?
# Difficulty Level: L2

# Obtain the column name with the highest number of row-wise maximum’s in df.


df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1))
display(df)
def largest_value_col_row_wise(df):
    tmp = df.copy()
    result_col = []
    for row in range(tmp.shape[0]):
        max_idx = tmp.iloc[row,:].idxmax()
        result_col.append(tmp.columns[max_idx])
    return result_col
result = largest_value_col_row_wise(df)
result

# Hint, pd.Series.argmax 要被棄用了 使用idxmax替代


# +
# 60. How to create a new column that contains the row number of nearest column by euclidean distance?
# Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.

# Difficulty Level: L3

df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
display(df.head())

# more readable
def get_neast_and_euclidean_dist(df):
    from scipy.spatial.distance import pdist, squareform
    row_name = df.index.tolist()
    dist = pdist(df, 'euclidean')
    df_dist = pd.DataFrame(squareform(dist), columns=row_name, index=row_name)
    
    nearest_list = []
    nearest_dist_list = []
    # instead of list comprehension
    # for loop is more readable for complex operation
    for row in df_dist.index:
        nearest_info = df_dist.loc[row, :].sort_values()
        nearest_idx, nearest_dist = nearest_info.index[1], nearest_info.values[1]
        nearest_list.append(nearest_idx)
        nearest_dist_list.append(nearest_dist)
    df_dist['nearset'] = nearest_list
    df_dist['dist'] = nearest_dist_list
    
    return df_dist
get_neast_and_euclidean_dist(df)

# when to use
# 計算距離時, pdist, squareform
# 提供了非常多基於numpy計算的距離，包含euclidean, cosine, correlation,
# hamming, 等等, 非常實用
# + {}
# 61. How to know the maximum possible correlation value of each column against other columns?
# Difficulty Level: L2

# Compute maximum possible absolute correlation value of each column against other columns in df.

df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1), columns=list('pqrstuvwxy'), index=list('abcdefgh'))

corr_df = abs(df.corr())
max_corr_list = [(feature, 
                  (corr_df[feature].sort_values(ascending=False).index[1],
                   corr_df[feature].sort_values(ascending=False)[1]))
                 for feature in corr_df.columns]
max_corr_list


# +
# 62. How to create a column containing the minimum by maximum of each row?
# Difficulty Level: L2

# Compute the minimum-by-maximum for every row of df.

df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

# Vectorlized

df['RowMinByMax'] = df.min(axis=0) / df.max(axis=0)
df.head()

# +
# 63. How to create a column that contains the penultimate value in each row?
# Difficulty Level: L2

# Create a new column 'penultimate' which has the second largest value of each row of df.
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

row_penultimate_collection = []
for row in df.index:
    row_penultimate = df.loc[row,:].sort_values().iloc[1]
    row_penultimate_collection.append(row_penultimate)
df['Row_Penultimate'] = row_penultimate_collection
df.head()

# +
# 64. How to normalize all columns in a dataframe?
# Difficulty Level: L2
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

# vectorlized
def Nomolize_df(df, minmax=False):
    tmp = df.copy()
    for col in tmp.columns:
        if not minmax:
            mean = tmp[col].mean()
            std = tmp[col].std()
            tmp[col] = (tmp[col] - mean) / std
        min_col = tmp[col].min()
        max_col = tmp[col].max()
        tmp[col] = (max_col - tmp[col]) / (max_col - min_col)
    return tmp

df_nor = Nomolize_df(df)
df_minmax = Nomolize_df(df, minmax=True)
display(df_nor,
       df_minmax)

# +
# 65. How to compute the correlation of each row with the suceeding row?
# Difficulty Level: L2

# Compute the correlation of each row of df with its succeeding row.

df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

corr_list = []
for first_row_idx, second_row_idx in zip(df.index[:-1],
                                         df.index[1:]):
    first_row = df.iloc[first_row_idx,:]
    second_row = df.iloc[second_row_idx,:]

    corr_list.append(
        (first_row_idx, second_row_idx, first_row.corr(second_row))
    )
corr_list

# +
# 66. How to replace both the diagonals of dataframe with 0?
# Difficulty Level: L2

# Replace both values in both diagonals of df with 0.

df = pd.DataFrame(np.random.randint(1,100, 100).reshape(10, -1))

# More readable
np.fill_diagonal(df.values, 0)

df
# hint
# np.fill_diagonal 沒有return值, 
# 因此 new_array = np.fill_diagonal(df.values, 0), new_array會為None
# pd.DataFrame.values 只能呼叫，無法直接帶入值
# 因此 df.vales = np.fill_diagonal(df.values, 0) 不會work
# -


