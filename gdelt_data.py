import gdelt

# Version 1 queries
# gd1 = gdelt.gdelt(version=1)

# # pull single day, gkg table
# results= gd1.Search('2016 Nov 01',table='gkg')
# print(len(results))

# pull events table, range, output to json format
# results = gd1.Search(['2016 Oct 30','2016 Oct 31'],coverage=True,table='events')
# print(len(results))

# Version 2 queries
gd2 = gdelt.gdelt(version=2)

# Single 15 minute interval pull, output to json format with mentions table
# results = gd2.Search('2016 Nov 1',table='events',output='csv', coverage=False)
# print((results))

# Full day pull, output to pandas dataframe, events table
# results = gd2.Search(['2016 11 01'],table='events',coverage=True)
# print(len(results))


'''
date = use [] to get a range date. exp. ['2020 01 01, 2020 02 01] is 1 Jan till 1 Feb of data
'''


# this code works (pulls data), had to change output=csv to df
# note: find a way to filter before pulling everything

results = gd2.Search(date=['2020 Jul 16'],  table='events', output='df', coverage=False)
#print(len(results[0]))
print(results.info())



t1 = results[['AvgTone', 'NumMentions', 'EventBaseCode', 'EventRootCode', 'ActionGeo_CountryCode']]
#print(t1)
print(t1['ActionGeo_CountryCode'].unique())

 