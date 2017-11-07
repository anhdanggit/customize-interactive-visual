
''' WEATHER PLOT '''

'''The plot uses the NOAA dataset, which is stoed in the 'data/'''


# The following variables are provided:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)

import matplotlib.pyplot as plt
import mplleaflet  # to install mplleaflet, open the anaconda prompt, and run > pip install mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('../data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# loading data
df = pd.read_csv('../data/BinnedCsvs_d400.csv')

# Cleaning data
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].apply(lambda x: x.year)
df['Month'] = df['Date'].apply(lambda x: x.month)
df['Day'] = df['Date'].apply(lambda x: x.strftime('%m%d'))
df = df[df['Day'] != '0229']  # remove leap day


# group TMAX by day of year from 2005-2014 (taking the record) 
temp_max = (df[(df['Element'] == 'TMAX') & (df['Year'] <= 2014) & (df['Year'] >= 2005)]
          .groupby(['Day'], as_index=True)['Data_Value']
          .max())
temp_max.index = range(1, 366)


# group TMIN by day of year from 2005-2014 (taking the record) 
temp_min = (df[(df['Element'] == 'TMIN') & (df['Year'] <= 2014) & (df['Year'] >= 2005)]
          .groupby(['Day'], as_index=True)['Data_Value']
          .min())
temp_min.index = range(1, 366)


# 2015 broken record points 
max_2015 = (df[(df['Element'] == 'TMAX') & (df['Year'] == 2015)]
          .groupby(['Day'], as_index=True)['Data_Value']
          .max())

max_2015.index = range(1, 366)
max_2015 = max_2015[max_2015 > temp_max]


min_2015 = (df[(df['Element'] == 'TMIN') & (df['Year'] == 2015)]
          .groupby(['Day'], as_index=True)['Data_Value']
          .min())
min_2015.index = range(1, 366)  # set index by day of year
min_2015 = min_2015[min_2015 < temp_min]


# Plot

plt.figure(figsize=(10, 4))

# plot the series of temp_max and temp_min
plt.plot(temp_max.index, temp_max, c='orange', alpha=0.5, linewidth=2)
plt.plot(temp_min.index, temp_min, c='green', alpha=0.5, linewidth=2)

# plot the broken point of 2015
plt.scatter(max_2015.index, max_2015, c='red', s=12)
plt.scatter(min_2015.index, min_2015, c='blue', s=12)


# fill the area between temp_max and temp_min
# using the current axes, the x is set as the index of series
plt.gca().fill_between(range(1,366), 
                       temp_max, temp_min,
                      facecolor='gray',
                      alpha=0.25)
# legend is not included for the lower ink-ratio, it is apparent the high and low lines

# change the label of y to degrees C
axes = plt.gca().axes
ylab = []
for item in axes.get_yticks():
    ylab.append(item/10)
plt.gca().set_yticklabels(ylab)

# get the first day of each month, not leap
xticks = ((pd.date_range('2015-01-01', '2015-12-31', freq='M')-1 + pd.Timedelta('1D'))
          .strftime('%j').astype(int))  # display as day in year
xticks_minor = ((pd.date_range('2015-01-01', '2015-12-31', freq='M')-1 + pd.Timedelta('15D'))
                .strftime('%j').astype(int))  # display as day in year

# change the format to month
xticks_label = pd.to_datetime(xticks, format='%j').strftime('%b')

# set the lim for xlim
axes.set_xlim(1, 365)
axes.set_xticks(xticks)
axes.set_xticklabels('')  # hide the major xticklabel
axes.set_xticks(xticks_minor, minor=True)
axes.set_xticklabels(xticks_label, minor=True) # show the label in the middle of month

# legend
plt.legend(['High-record', 'Low-record', 'Broken high-record 2015', 'Broken low-record 2015'], loc=8, frameon=False)


plt.ylabel('Degrees C')
plt.title('The record high and record low temperatures from 2005-2014 \n Ann Arbor, Michigan, United States')
plt.show()




